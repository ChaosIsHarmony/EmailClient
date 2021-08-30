import imapclient
from . import EmailParser


class ReceivingEmail:

    def __init__(self):
        self.imapObj = imapclient.IMAPClient("imap.gmail.com", ssl=True)


    def connect(self, username: str, password: str) -> str:
        status = self.imapObj.login(username, password)
        return status


    def fetch_unseen(self):
        self.imapObj.select_folder("INBOX", readonly=True)
        UIDs = self.imapObj.search(["UNSEEN"])
        rawMessage = EmailParser.parse_raw_message(self.imapObj.fetch([UIDs[-1]], ["BODY[]", "FLAGS"])[UIDs[-1]])
        # TODO: parse->display email


    def disconnect(self) -> None:
        self.imapObj.logout()
