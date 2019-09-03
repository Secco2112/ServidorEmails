from user import User

class MailServer:
    def __init__(self):
        self.users = []
        self.user_ai = 0

    def get_last_user_ai(self):
        return self.user_ai

    def user_exists(self, type, value):
        method = "get_" + type
        for user in self.users:
            method_call = getattr(user, method)
            if method_call() == value and not user.deleted():
                return True
        return False

    def get_user_by(self, type, value):
        method = "get_" + type
        for user in self.users:
            method_call = getattr(user, method)
            if method_call() == value and not user.deleted():
                return user
        return False

    def add_user(self, user):
        user.set_id(self.get_last_user_ai())
        self.users.append(user)
        self.user_ai += 1
        return self

    def create_user(self, name, email):
        if self.user_exists("email", email):
            return False
        else:
            user = User()
            user.set_name(name).set_email(email)
            self.add_user(user)
            return user

    def remove_user(self, type, value):
        method = "get_" + type
        for i,user in enumerate(self.users):
            method_call = getattr(user, method)
            if method_call() == value and not user.deleted():
                self.users[i].delete()
        return self

    def users_size(self):
        return len(self.users)

    def get_users(self):
        return self.users

    def menu(self):
        print("***********************************");
        print("*  Servidor de emails:            *");
        print("*  1. Cadastrar usuario           *");
        print("*  2. Remover usuario             *");
        print("*  3. Enviar mensagem             *");
        print("*  4. Ver mensagens               *");
        print("*  5. Mostrar informacoes         *");
        print("*  6. Sair                        *");
        print("***********************************\n");
