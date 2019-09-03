from mail_box import MailBox

class User:
    def __init__(self):
        self.__id = None
        self.__name = None
        self.__email = None
        self.__deleted = 0
        self.__inbox = MailBox()
        self.__sent = MailBox()
        self.__current_mailbox = None

    def set_id(self, id):
        self.__id = id
        return self

    def set_name(self, name):
        self.__name = name
        return self

    def set_email(self, email):
        self.__email = email
        return self

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def delete(self):
        self.__deleted = 1
        return self

    def deleted(self):
        return self.__deleted == 1

    def inbox(self):
        self.__current_mailbox = "inbox"
        return self

    def sent_box(self):
        self.__current_mailbox = "sent"
        return self

    def add_email(self, mail):
        if self.__current_mailbox == "inbox":
            self.__inbox.add(mail)
        elif self.__current_mailbox == "sent":
            self.__sent.add(mail)
        return self

    def get_box(self):
        if self.__current_mailbox == "inbox":
            return self.__inbox
        else:
            return self.__sent
