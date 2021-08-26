from datetime import date, datetime
import imapclient
import os

from . import Email
from . import EmailParser

HOST = "imap.gmail.com"
fileDir = os.path.dirname(os.path.realpath('__file__'))
creds_file = os.path.join(fileDir, 'misc/creds.ps')
creds_file = os.path.abspath(os.path.realpath(creds_file))

if __name__ == "__main__":
    with open(creds_file, 'r') as f:
        creds = f.read().splitlines()
    # LOGIN
    username = creds[0]#input("Username: ")
    password = creds[1]#input("Password: ")
    imapObj = imapclient.IMAPClient(HOST, ssl=True)
    imapObj.login(username, password)
    # FETCH UNSEEN EMAILS
    imapObj.select_folder("INBOX", readonly=True)
    UIDs = imapObj.search(["UNSEEN"])
    rawMessage = EmailParser.parse_raw_message(imapObj.fetch([UIDs[-1]], ["BODY[]", "FLAGS"])[UIDs[-1]])
    # LOGOUT
    imapObj.logout()
