# NUS Temperature Declaration Script

This is a python port of [this script](https://github.com/jiachen247/nus-htd-automation) to
easily submit your temperature to NUS's temperature declaration system.

## How to download

```bash
$ git clone https://github.com/chrisgzf/nus-temp
$ cd nus-temp
$ python Declare.py
```

OR just download `Declare.py` using your web-browser and run it.

## How to use

To run the script, simply run:
```bash
$ python Declare.py
```
On your first run, you will set-up your NUSNET credentials.

On your subsequent runs, running this script will immediately submit a randomly-generated
temperature. Please note that this is only for testing! Do submit your actual temperature
with
```bash
$ python Declare.py <your temp here>
```

To see what options there are, run:
```bash
$ python Declare.py -h
```

The options that are available are:
```
usage: Declare.py [-h] [-v] [-d DATE] [-t TIME] [-s SYM] [TEMP]

Submits NUS temperature declaration

positional arguments:
  TEMP                  temperature you would like to declare. leave blank for random (default: 36.3)

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         verbose - enable debug messages (default: False)
  -d DATE, --date DATE  date in DD/MM/YYYY. defaults to today's date (default: 27/03/2020)
  -t TIME, --time TIME  time of day - 'A' or 'P'. defaults to current time (default: A)
  -s SYM, --sym SYM     whether you have symptoms - 'Y' or 'N'. defaults to no (default: N)
```

## Disclaimer

1. This script stores your NUSNET credentials in plaintext in a file called `creds.txt`. If you
are uncomfortable with your credentials being stored in such a manner, either (1) make a PR to
implement a better way, or (2) don't use this.
1. The aim of this tool is to make it fast and easy to submit your temperature declaration. You
may have noticed that if you simply run `python Declare.py` without any arguments, a random
temperature is generated and submitted. This is only for testing purposes! Please do use this
script as a means of helping you to submit your actual body temperature!
1. This script works at the time of publishing this, but it is your onus to check if the right
temperatures have been recorded on the portal. I **will not be responsible** if the script breaks,
and you end up not submitting your temperature declaration on time.

## Credits

Credits to [@jiachen247](https://github.com/jiachen247/nus-htd-automation) for writing the initial
JavaScript version of the script.
