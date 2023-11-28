import datetime
import csv
from dateutil import parser


def write_to_file(line):
    with open("historical-data.csv", "a", newline='', ) as historical_data:
        writer = csv.writer(historical_data)
        writer.writerow("")
        writer.writerow(line)


def erase_stray_date():
    with open("historical-data.csv", "r+") as historical_data:
        lines = historical_data.readlines()
        lines.pop()
        historical_data_writer = open('historical-data.csv', "w+")
        historical_data_writer.writelines(lines)


def parse_date_from_command_line(date):
    try:
        if date.lower() == "today":
            return datetime.datetime.today().date()
        else:
            return parser.parse(date).date()
    except:
        print("Format violation. Please enter the date in the YYYY-MM-DD format or type \"today\": ")
