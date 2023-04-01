import smtplib

my_email = ""
password = ""
recipient_email = ""

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=recipient_email,
                        msg="Subject:Hello\n\nThis is the body of my email.")
