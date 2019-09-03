class Mail:
    def __init__(self):
        self.__origin_id = None
        self.__target_id = None
        self.__subject = None
        self.__message = None

    def set_origin_id(self, origin_id):
        self.__origin_id = origin_id
        return self

    def set_target_id(self, target_id):
        self.__target_id = target_id
        return self

    def set_subject(self, subject):
        self.__subject = subject
        return self

    def set_message(self, message):
        self.__message = message
        return self

    def get_origin_id(self):
        return self.__origin_id

    def get_target_id(self):
        return self.__target_id

    def get_subject(self):
        return self.__subject

    def get_message(self):
        return self.__message
