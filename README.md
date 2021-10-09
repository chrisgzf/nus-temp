# NUS Temperature Declaration Script

This is a python port of [this script](https://github.com/jiachen247/nus-htd-automation) to
easily submit your temperature to NUS's temperature declaration system.

## How to download

```bash
$ git clone https://github.com/chrisgzf/nus-temp
$ cd nus-temp
$ python declare.py
```

OR just download `declare.py` using your web-browser and run it.

## How to use

To run the script, simply run:
```bash
$ python declare.py
```
On your first run, you will set-up your NUSNET credentials.

On your subsequent runs, running this script will immediately submit a randomly-generated
temperature. Please note that this is only for testing! Do submit your actual temperature
with
```bash
$ python declare.py <your temp here>
```

To see what options there are, run:
```bash
$ python declare.py -h
```

The options that are available are:
```
usage: declare.py [-h] [-v] [-t TIME] [-s SYM] [TEMP]

Submits NUS temperature declaration

positional arguments:
  TEMP                  temperature you would like to declare. leave blank for random (default: 36.3)

optional arguments:
  -h, --help                   show this help message and exit
  -v, --verbose                verbose - enable debug messages (default: False)
  -t TIME, --time TIME         time of day - 'A' or 'P'. defaults to current time (default: A)
  -s SYM, --sym SYM            whether you have symptoms - 'Y' or 'N'. defaults to no (default: N)
  -f FAMSYM, --famsym FAMSYM   whether someone in the same household with symptoms - 'Y' or 'N'. defaults to no (default: N)
```

## Use as Github Action

1. Fork this repo
2. In **your own** fork, under Settings-Secrets, add two secrets: `TEMP_DECLARE_USERNAME` and `TEMP_DECLARE_PASSWORD`
3. Uncomment `schedule` section in `.github/workflows/main.yml` and configure your preferred declaration time
4. Check under Actions, there is an action called "declare". You may manually run the action once to see if it works

## Disclaimer

1. This script stores your NUSNET credentials in plaintext in a file called `creds.txt`. If you
are uncomfortable with your credentials being stored in such a manner, either (1) make a PR to
implement a better way, or (2) don't use this.
2. The aim of this tool is to make it fast and easy to submit your temperature declaration. You
may have noticed that if you simply run `python declare.py` without any arguments, a random
temperature is generated and submitted. This is only for testing purposes! Please do use this
script as a means of helping you to submit your actual body temperature!
3. This script works at the time of publishing this, but it is your onus to check if the right
temperatures have been recorded on the portal. I **will not be responsible** if the script breaks,
and you end up not submitting your temperature declaration on time.
4. If you opted to deploy this script as a GitHub action, you should always remember to turn off
the script and report your status accordingly as soon as you have symptoms or have someone in the
same household with symptoms. I **will not be responsible** if you face any displinary actions or
even criminal charges if your declaration is false due to the automatic action.

## Credits

Credits to [@jiachen247](https://github.com/jiachen247/nus-htd-automation) for writing the initial
JavaScript version of the script.
