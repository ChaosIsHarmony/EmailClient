from typing import List

class EmailMessage():
    '''
    Defines the viewable and editable contents of an email.
    '''
    def set_uid(self, uid: int) -> None:
        self.uid = uid


    def get_uid(self) -> int:
        return self.uid


    def set_date(self, date: str) -> None:
        self.date = date


    def get_date(self) -> str:
        return self.date


    def set_subject(self, subject: str) -> None:
        self.subject = subject


    def get_subject(self) -> str:
        return self.subject


    def set_sender(self, sender: str) -> None:
        self.sender = sender


    def get_sender(self) -> str:
        return self.sender


    def set_recipients(self, recipients: List[str]) -> None:
        self.recipients = recipients


    def get_recipients(self) -> List[str]:
        return self.recipients

    def set_body(self, body: str) -> None:
        self.body = body


    def get_body(self) -> str:
        return self.body


    def __repr__(self) -> str:
        email = self.subject + "\n\n"
        email += self.sender + "\n\n"
        email += self.body
        return email
