from getpass import getpass

from models.user import User

if __name__ == '__main__':
    print("Hello, this is the Autenticação Hash app")
    print("We will now create a new user for you")

    user: User

    while True:
        try:
            name = input("What is your name? ")
            email = input("What is your email? ")
            password = getpass(prompt='What is your password? ')

            user = User(name, email, password)
            break
        except ValueError as e:
            print(e)

    print(f'Hi {user.nome}')
    save = input("Would you like to save the user?(Y/n) ")

    if save.lower() == "y" or save.lower() == "yes":
        user.save_user()