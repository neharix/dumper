import datetime
import os
import smtplib
import subprocess
import time
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import pytz
import schedule

os.environ["PGPASSWORD"] = "your postgresql database password"


def send_mail(fromaddr: str, toaddr: list, file_path: str):
    for address in toaddr:
        now = datetime.datetime.now(
            tz=pytz.timezone("Asia/Ashgabat")
        )  # you can change it to your time zone
        message = MIMEMultipart()
        message["From"] = fromaddr
        message["To"] = address
        message["Subject"] = f'[{now.strftime("%d-%m-%Y")}]: Enter your subject text'
        message.attach(
            MIMEText(f"Sent time: {now.strftime('%d.%m.%Y %H:%M:%S')}", "plain")
        )
        file_name = f"data-{now.strftime('%d-%m-%Y')}.sql"
        with open(file_path, "r") as sql_file:
            attachment = sql_file.read()
        file_base = MIMEBase("plain", "application")
        file_base.set_payload(attachment)
        encoders.encode_base64(file_base)
        file_base.add_header("Content-Disposition", f"attachment; filename={file_name}")
        message.attach(file_base)
        smtp_session = smtplib.SMTP("smtp.gmail.com", 587)
        smtp_session.starttls()
        smtp_session.login(
            fromaddr, "iiii iiii iiii iiii"
        )  # change it to your app password
        mail_text = message.as_string()
        smtp_session.sendmail(fromaddr, address, mail_text)

        smtp_session.quit()
    os.remove("data.sql")


def get_dump():
    subprocess.run(
        [
            "pg_dump",
            "-f",
            "data.sql",
            "-h",
            "database_host",  # FIXME
            "-U",
            "database_user",  # FIXME
            "-d",
            "database_name",  # FIXME
            "-p",
            "database_port",  # FIXME
        ]
    )
    send_mail("your app email", ["list", "of", "recipients"], "data.sql")


schedule.every().day.at("00:00").do(get_dump)  # you can also set the sending time

while True:
    schedule.run_pending()
    time.sleep(1)
