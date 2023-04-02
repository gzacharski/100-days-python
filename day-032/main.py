import smtplib
import datetime as dt
import random

my_email = ""
password = ""
recipient_email = ""

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 6:
    with open("quotes.txt", "r") as quotes:
        lines = quotes.readlines()

    chosen_line = random.choice(lines)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=recipient_email,
                            msg=f"Subject:Monday Motivation\n\n{chosen_line}")
else:
    print("No email sent. Wait till Monday")
