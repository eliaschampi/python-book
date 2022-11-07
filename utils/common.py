from termcolor import colored


def showWelcome() -> None:
    print(colored("Bienvenido a tu programa", "blue"))
    print("****" * 5)


def showGoodBye() -> None:
    print(colored("Hasta pronto!", "blue"))
    exit()
