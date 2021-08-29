from datetime import date, datetime
import os

from .Email import Email
from .ReceivingEmail import ReceivingEmail
from .SendingEmail import SendingEmail

fileDir = os.path.dirname(os.path.realpath('__file__'))
creds_file = os.path.join(fileDir, 'misc/creds.ps')
creds_file = os.path.abspath(os.path.realpath(creds_file))


def receive_email(username: str, password: str) -> None:
    pass



def send_email(username: str, password: str) -> None:
    sendEmail = SendingEmail()
    status = sendEmail.connect(username, password)
    print(status)
    sendEmail.disconnect()




if __name__ == "__main__":
    # READ IN CREDENTIALS
    with open(creds_file, 'r') as f:
        creds = f.read().splitlines()

    username = creds[0]#input("Username: ")
    password = creds[1]#input("Password: ")

    # DETERMINE USE CASE
    use = None
    while use == None:
        try:
            use = int(input("Select Use:\n\n\t1. Receive\n\t2. Send\n"))
        except:
            print("Invalid selection.")

    if use == 2:
        send_email(username, password)

