import smtplib

class SendingEmail:

    def __init__(self):
        self.smtpObj = smtplib.SMTP("smtp.gmail.com", 587)


    def connect(self, email_address: str, password: str) -> bool:
        self.smtpObj.ehlo()
        self.smtpObj.starttls()
        status = self.smtpObj.login(email_address, password)
        if status[0] == 235:
            return True
        else:
            return False


    def disconnect(self) -> None:
        self.smtpObj.quit()

