from book.Book import Book
from book.app import showMenu, callAction
from utils.common import showWelcome, showGoodBye
from termcolor import colored


def main(bookinstance: Book) -> bool:

    if callAction(showMenu(), bookinstance):
        msg = colored("Volver al menu (si/no) por omision (si) => ", "yellow")
        return (input(msg) or "si") == "si"

    return False


if __name__ == "__main__":

    # show welcome message
    showWelcome()

    # start book instance
    bookinstance: Book = Book()

    willBeContinue = True

    while willBeContinue:

        willBeContinue = main(bookinstance)

    else:

        showGoodBye()
