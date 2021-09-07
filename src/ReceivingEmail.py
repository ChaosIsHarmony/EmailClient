import imapclient
import pprint
from typing import List

from .EmailMessage import EmailMessage
from . import EmailParser


class ReceivingEmail:

    def __init__(self, filter_vals: List[str]):
        self.imapObj = imapclient.IMAPClient("imap.gmail.com", ssl=True)
        self.emails = []
        self.pp = pprint.PrettyPrinter(indent='2')
        self.filter_vals = filter_vals


    def connect(self, username: str, password: str) -> str:
        status = self.imapObj.login(username, password)
        return status


    def fetch_unseen(self) -> List[EmailMessage]:
        self.imapObj.select_folder("INBOX", readonly=True)
        UIDs = self.imapObj.search(["UNSEEN"])
        for UID in UIDs:
            email = EmailParser.parse_raw_message(UID, self.imapObj.fetch([UID], ["BODY[]", "FLAGS"])[UID])
            for address in self.filter_vals:
                if address in email.get_sender():
                    self.emails.append(email)

        return self.emails


    def read_email(self) -> None:
        try:
            uid = int(input("Enter email UID: "))
        except:
            print("Invalid UID.")
            return

        for email in self.emails:
            if email.get_uid() == uid:
                print(email.get_body())
                return

        print("UID not found.")



    def delete_email(self) -> None:
        pass



    def disconnect(self) -> None:
        self.imapObj.logout()
