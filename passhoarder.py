import argparse
import csv

def read_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def clean(output_file):
    with open(output_file, 'r') as file:
        lines = file.readlines()
    unique_lines = set(lines)
    with open(output_file, 'w') as file:
        file.writelines(unique_lines)

def extract(emailpassFile, validusersFile, output_file):
    list1 = read_file(emailpassFile)
    list2 = read_file(validusersFile)
    email_password_dict = {}
    print("\nManually Add Preferred Password for Multiple Enteries\n")

# process email:pass
    for entry in list1:
        email, password = entry.split(':')
        if email in email_password_dict:
            email_password_dict[email].append(entry)
        else:
            email_password_dict[email] = [entry]

    # check for valid emails in email:pass
    with open(output_file, 'w') as output:
        for email in list2:
            if email in email_password_dict:
                matching_entries = email_password_dict[email]
                if len(matching_entries) > 1:
                    print(f"Multiple Enteries Found for: {email}")
                    for entry in matching_entries:
                        print(f"  {entry}")
                else:
                    output.write(f"{matching_entries[0]}\n")
    clean(output_file)

def parse(input_csv, output_file, user_column, password_column):
    with open(input_csv, 'r') as csv_file:
        reader = csv.reader(csv_file)
        with open(output_file, 'w') as output:
            for row in reader:
                if len(row) > max(user_column, password_column):
                    email = row[user_column]
                    password = row[password_column]

                    # skip empty passwords
                    if password:
                        output.write(f"{email}:{password}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract from CSV or parse email and password information.')
    subparsers = parser.add_subparsers(dest='command', help='Choose between userdump (dump from user:email) and parse commands (create email:pass from CSV)')

    # extract valid users / userdump args
    extract_parser = subparsers.add_parser('userdump', help='Extract your valid emails and passwords from email:pass')
    extract_parser.add_argument('-emailpass', dest='emailpassFile', required=True, help='File containing email:pass')
    extract_parser.add_argument('-valid', '-v', dest='validusersFile', required=True, help='File containing validated users')
    extract_parser.add_argument('-o', dest='output_file', required=True, help='Output file name')

    # create user:pass file / parse args
    parse_parser = subparsers.add_parser('parse', help='Parse Hoard CSV file and create file in email:pass format')
    parse_parser.add_argument('-in', dest='input_csv', required=True, help='Path to the Hoard CSV')
    parse_parser.add_argument('-out', dest='output_file', required=True, help='Output file name')
    parse_parser.add_argument('-uc', dest='user_column', type=int, default=0, help='User column (default is 0)')
    parse_parser.add_argument('-pc', dest='password_column', type=int, default=1, help='Password column (default is 1)')

    args = parser.parse_args()

    if args.command == 'userdump':
        extract(args.emailpassFile, args.validusersFile, args.output_file)
    elif args.command == 'parse':
        parse(args.input_csv, args.output_file, args.user_column, args.password_column)
    else:
        print("Invalid command. Use 'userdump' or 'parse'.")
