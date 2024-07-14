import smtplib
from email.mime.text import MIMEText

email_settings = {
    "smtp_server": "smtp.example.com",
    "port": 587,
    "username": "your_username",
    "password": "your_password"
}


def update_email_settings(settings):
    global email_settings
    email_settings.update(settings)
    return email_settings


def get_email_settings():
    return email_settings


def send_email(manual_send):
    msg = MIMEText(manual_send["body"])
    msg['Subject'] = manual_send["subject"]
    msg['From'] = email_settings["username"]
    msg['To'] = manual_send["to"]

    with smtplib.SMTP(email_settings["smtp_server"], email_settings["port"]) as server:
        server.login(email_settings["username"], email_settings["password"])
        server.sendmail(msg['From'], [msg['To']], msg.as_string())
    return {"message": "Email sent"}
