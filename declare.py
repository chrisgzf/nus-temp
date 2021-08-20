#!/usr/bin/env python3

import os
import sys
import random
import time
import logging
import getpass
import base64
import argparse
import requests
from datetime import datetime


def get_date():
    return datetime.today().strftime("%d/%m/%Y")


def get_time_of_day():
    hr = int(datetime.today().strftime("%H"))
    return "P" if hr >= 12 else "A"


def auth_and_get_cookie(user, password):
    VAFS_CLIENT_ID = "97F0D1CACA7D41DE87538F9362924CCB-184318"
    endpoint = "https://vafs.nus.edu.sg/adfs/oauth2/authorize"

    params = {
        "response_type": "code",
        "client_id": VAFS_CLIENT_ID,
        "resource": "sg_edu_nus_oauth",
        "redirect_uri": "https://myaces.nus.edu.sg:443/htd/htd"
    }

    data = {
        "UserName": "nusstu\\" + user,
        "PassWord": password,
        "AuthMethod": "FormsAuthentication"
    }

    logging.debug("Authenticating with VAFS")
    response = requests.post(endpoint, params=params, data=data)
    if response.status_code != 200 or "JSESSIONID" not in response.cookies:
        logging.error(
            "Unable to authenticate with VAFS. Are your NUSNET credentials correct?"
        )
        sys.exit(1)
    else:
        logging.debug("VAFS successfully authenticated")
        return response.cookies["JSESSIONID"]


def submit_temp(date, time_of_day, sympt_flag, fam_sympt_flag, cookie):
    cookie = {"JSESSIONID": cookie}
    endpoint = "https://myaces.nus.edu.sg/htd/htd"
    data = {
        "actionName": "dlytemperature",
        "tempDeclOn": date,
        "declFrequency": time_of_day,
        "symptomsFlag": sympt_flag,
        "familySymptomsFlag": fam_sympt_flag
    }

    logging.info(
        f"Submitting for {time_of_day}M on {date} (Symptoms: {sympt_flag}, Same household with symptoms: {fam_sympt_flag})"
    )
    response = requests.post(endpoint, cookies=cookie, data=data)

    if response.status_code != 200:
        logging.error("Failed to declare temperature. HTTP Error Code: " +
                      response.status_code)
        sys.exit(1)
    else:
        logging.info("Submitted successfully")


def get_credentials():
    logging.info(
        "NUSNET credentials not found. Creating a new credential file")
    print("\nWARNING: Your NUSNET credentials will be saved in plaintext.\n"
          "This has to be done so that the script can log you in.\n")

    password, verify = "", "_"
    while password != verify:
        print(
            "Please enter your NUSNET username (e0123456, without the nusstu\\): "
        )
        user = input()
        print(
            "Please enter your NUSNET password and press enter (you will not see what you've typed)"
        )
        password = getpass.getpass()
        print("Again")
        verify = getpass.getpass()
        if (password != verify):
            print("Passwords did not match!\n")

    with open("creds.txt", "wb+") as f:
        f.write(base64.b64encode(user.encode("ascii")) + b"\n")
        f.write(base64.b64encode(password.encode("ascii")))

    logging.info("Saved NUSNET credentials in creds.txt")
    return user, password


def read_credentials():
    if not os.path.exists("creds.txt"):
        return get_credentials()
    else:
        with open("creds.txt", "rb") as f:
            user = base64.b64decode(f.readline()).decode("ascii").strip()
            password = base64.b64decode(f.readline()).decode("ascii").strip()
        return user, password


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Submits NUS temperature declaration",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-v",
                        "--verbose",
                        help="verbose - enable debug messages",
                        action="store_true")
    parser.add_argument(
        "-t",
        "--time",
        type=str,
        help="time of day - 'A' or 'P'. defaults to current time",
        default=get_time_of_day())
    parser.add_argument(
        "-s",
        "--sym",
        type=str,
        help="whether you have symptoms - 'Y' or 'N'. defaults to no",
        default="N")
    parser.add_argument(
        "-f",
        "--famsym",
        type=str,
        help="whether someone in the same household with symptoms - 'Y' or 'N'. defaults to no",
        default="N")
    parser.add_argument("--no-random-timer", action="store_true")
    args = parser.parse_args()
    logging.basicConfig(format="[%(levelname)s] %(asctime)s: %(message)s",
                        datefmt="%d/%m/%Y %I:%M:%S %p",
                        level=logging.DEBUG if args.verbose else logging.INFO,
                        handlers=[
                            logging.FileHandler("temp.log", "a"),
                            logging.StreamHandler()
                        ])

    user, password = read_credentials()
    if not args.no_random_timer:
        time.sleep(random.randrange(180, 1000))
    session_cookie = auth_and_get_cookie(user, password)
    submit_temp(date=get_date(),
                time_of_day=args.time,
                sympt_flag=args.sym,
                fam_sympt_flag=args.sym,
                cookie=session_cookie)
