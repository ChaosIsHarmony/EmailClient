class Email():
    '''
    Defines the viewable and editable contents of an email.
    '''
    def set_uid(self, uid: int) -> None:
        self.uid = uid


    def get_uid(self) -> int:
        return self.uid


    def set_title(self, title: str) -> None:
        self.title = title


    def get_title(self) -> str:
        return self.title


    def set_sender(self, sender: str) -> None:
        self.sender = sender


    def get_sender(self) -> str:
        return self.sender


    def set_body(self, body: str) -> None:
        self.body = body


    def get_body(self) -> str:
        return self.body


    def __repr__(self) -> str:
        email = self.title + "\n\n"
        email += self.sender + "\n\n"
        email += self.body
        return email
