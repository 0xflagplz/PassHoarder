# PassHoarder

PassHoarder is a lightweight tool for extracting valid users and passwords from email:password files or parsing CSV dump files to create a file in email:password format.

## Installation

No installation is required. Simply download the script and ensure you have Python installed.

## Usage

### Create a email:pass file using a CSV. Specify specific columns if neccessary. (Reminder, the first column is 0)
```bash
└─$ python3 passhoarder.py parse -in csvdumpFile -out outfile -uc 0 -pc 2

usage: passhoarder.py parse [-h] -in INPUT_CSV -out OUTPUT_FILE [-uc USER_COLUMN] [-pc PASSWORD_COLUMN]

options:
  -h, --help            show this help message and exit
  -in INPUT_CSV, -i INPUT_CSV
                        Path to the Hoard CSV
  -out OUTPUT_FILE, -o OUTPUT_FILE
                        Output file name
  -uc USER_COLUMN       User column (default is 0)
  -pc PASSWORD_COLUMN   Password column (default is 1)
```
### Extract valid emails and passwords using a validated list. Repeats will need to be added manually (avoid lockouts).
```bash
└─$ python3 passhoarder.py userdump -emailpass dumpfile.txt -v validemails.txt -o output.txt

usage: passhoarder.py userdump [-h] -emailpass EMAILPASSFILE -valid VALIDUSERSFILE -o OUTPUT_FILE

options:
  -h, --help            show this help message and exit
  -emailpass EMAILPASSFILE
                        File containing email:pass
  -valid VALIDUSERSFILE, -v VALIDUSERSFILE
                        File containing validated users
  -o OUTPUT_FILE        Output file name
```
