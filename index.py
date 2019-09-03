from mail_server import MailServer
from user import User
from mail import Mail

mail_server = MailServer();

#Cria usuários iniciais
user = User()
mail_server.create_user("Gustavo Marmentini", "gustavo@astrusweb.com")
mail_server.create_user("SALIMZÃO", "salim@astrusweb.com")

while True:
    mail_server.menu()

    option = int(input("Digite o valor da opção que deseja: "))
    while option < 1 or option > 6:
        option = int(input("Opção inválida. Digite um valor entre 1 e 6: "))

    if option == 1:
        print("\nCadastro de usuário:")
        name = input("Digite o nome do usuário: ")
        email = input("Digite o email do usuário: ")
        handle = mail_server.create_user(name, email)
        if handle:
            print("Usuário com id", handle.get_id(), "criado com sucesso!\n\n")
        else:
            print("Um usuário com o email", email, "já existe\n\n")

    elif option == 2:
        print("\nRemoção de usuário:")
        id = int(input("Digite o id do usuário que deseja remover: "))
        if mail_server.user_exists("id", id):
            handle = mail_server.get_user_by("id", id)
            mail_server.remove_user("id", id)
            print("Usuário", handle.get_name() + " <" + handle.get_email() + "> removido com sucesso!\n\n")
        else:
            print("Não existe um usuário com o id especificado\n\n")

    elif option == 3:
        origin_id = int(input("Digite o id do usuário que vai enviar a mensagem: "))
        while not mail_server.user_exists("id", origin_id):
            origin_id = int(input("O usuário com o id especificado não foi encontrado. Digite novamento o id do usuário que vai enviar a mensagem: "))
        target_id = int(input("Digite o id do usuário que vai receber a mensagem: "))
        while not mail_server.user_exists("id", target_id):
            target_id = int(input("O usuário com o id especificado não foi encontrado. Digite novamento o id do usuário que vai receber a mensagem: "))

        subject = input("Digite o assunto do email: ")
        message = input("Digite a mensagem do email: ")

        mail = Mail()
        mail.set_origin_id(origin_id)
        mail.set_target_id(target_id)
        mail.set_subject(subject)
        mail.set_message(message)

        mail_server.get_user_by("id", origin_id).inbox().add_email(mail)
        mail_server.get_user_by("id", target_id).sent_box().add_email(mail)
        print("\n\n")
    elif option == 4:
        user_id = int(input("Digite o id do usuário que deseja visualizar as mensagens: "))
        while not mail_server.user_exists("id", user_id):
            user_id = int(input("Digite o id do usuário que deseja visualizar as mensagens: "))

        print("1 - Caixa de entrada\n2 - Caixa de saída")
        box_id = int(input("Selecione o id da caixa: "))
        while box_id < 1 or box_id > 2:
            box_id = int(input("Selecione o id da caixa: "))

        if box_id == 1:
            emails = mail_server.get_user_by("id", user_id).sent_box().get_box().get_emails()
        else:
            emails = mail_server.get_user_by("id", user_id).inbox().get_box().get_emails()

        print("Quantidade de emails: %d" %len(emails))
        print("---------------------------------------------------------------------------------------------")
        for email in emails:
            origin_user = mail_server.get_user_by("id", email.get_origin_id())
            target_user = mail_server.get_user_by("id", email.get_target_id())
            print("De: %s <%s>" %(origin_user.get_name(), origin_user.get_email()))
            print("Para: %s <%s>" % (target_user.get_name(), target_user.get_email()))
            print("Assunto: %s" %email.get_subject())
            print("Mensagem:")
            print(email.get_message() + "\n\n")

    elif option == 5:
        users = mail_server.get_users()
        for user in users:
            print("\nID: %d" %user.get_id())
            print("Nome: %s" %user.get_name())
            print("Email: %s" %user.get_email())
            print("Número de mensagens na caixa de entrada: %d" %len(user.inbox().get_box().get_emails()))
            print("Número de mensagens na caixa de saída: %d\n" % len(user.sent_box().get_box().get_emails()))
        print("")

    elif option == 6:
        print("\nObrigado por utilizar o servidor de emails!")
        exit()