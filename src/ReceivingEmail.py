import imapclient
from . import EmailParser


class ReceivingEmail:

    def __init__(self):
        self.imapObj = imapclient.IMAPClient("imap.gmail.com", ssl=True)


    def connect(username: str, password: str) -> bool:
        imapObj.login(username, password)
        # TODO: check status
        return True


    def fetch_unseen():
        imapObj.select_folder("INBOX", readonly=True)
        UIDs = imapObj.search(["UNSEEN"])
        rawMessage = EmailParser.parse_raw_message(imapObj.fetch([UIDs[-1]], ["BODY[]", "FLAGS"])[UIDs[-1]])
        # TODO: parse->display email

    def disconnect() -> None:
        imapObj.logout()
