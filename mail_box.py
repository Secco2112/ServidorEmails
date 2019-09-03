class MailBox:
    def __init__(self):
        self.emails = []

    def add(self, mail):
        self.emails.append(mail)
        return self

    def get_emails(self):
        return self.emails