##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import random
import smtplib
import pandas
import datetime as dt

LETTER_TEMPLATES = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]

my_email = ""
password = ""


def provide_birthday_list():
    now = dt.datetime.now()
    current_day = now.day
    current_month = now.month

    data_frame = pandas.read_csv("birthdays.csv")
    return [record for record in data_frame.to_dict("records") if
            record.get('month') == current_month and record.get('day') == current_day]


def provide_email_content(name: str):
    letter_path = random.choice(LETTER_TEMPLATES)
    with open(letter_path) as letter:
        lines = letter.readlines()
        return "".join(lines).replace("[NAME]", name)


def send_email(recipient_email: str, msg_content: str):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=recipient_email,
                            msg=f"Subject:Happy Birthday\n\n{msg_content}")


today_birthday_list = provide_birthday_list()
recipient_list = [{"recipient_email": record.get('email'), "msg_content": provide_email_content(record.get('name'))} for
                  record in
                  today_birthday_list]

for recipient in recipient_list:
    send_email(recipient_email=recipient.get("recipient_email"), msg_content=recipient.get("msg_content"))
