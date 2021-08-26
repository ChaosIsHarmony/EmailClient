import imapclient
from datetime import date, datetime

HOST = "imap.gmail.com"

if __name__ == "__main__":
    # LOGIN
    username = input("Username: ")
    password = input("Password: ")
    imapObj = imapclient.IMAPClient(HOST, ssl=True)
    imapObj.login(username, password)
    # FETCH UNSEEN EMAILS
    imapObj.select_folder("INBOX", readonly=True)
    UIDs = imapObj.search(["UNSEEN"])
    rawMessage = imapObj.fetch([UIDs[-1]], ["BODY[]", "FLAGS"])
    # DISPLAY MOST RECENT
    print(rawMessage)
    # LOGOUT
    imapObj.logout()
