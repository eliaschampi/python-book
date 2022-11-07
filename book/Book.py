from utils.decorators import listToDict, dictToStrLine
from utils.constants import DB_SEPARATOR
from utils.validation import validateBookItem

class Book:

    __SEP = DB_SEPARATOR

    def __init__(self) -> None:
        self.books = []

    def __strToList(self, row: str) -> list:
        return row.split(self.__SEP)

    def loadBooks(self, db: str) -> None:

        books = []
        try:

            with open(db, "r") as lines:

                title = self.__strToList(next(lines))

                books = [listToDict(title, self.__strToList(row)) for row in lines]
        except:
            print("Ocurrión un error al cargar la base de datos local")
            exit()
        finally:
            self.books = books

    def getAll(self) -> list:
        return self.books

    def addBook(self, bookItem: dict):

        message, validated = validateBookItem(bookItem)

        if not validated:
            return message, False
        print(message)
        self.books.append(bookItem)
        return "Correctamente agregado", True

    def findByParam(self, finder: str):
        print(self.books)
        return list(filter(lambda item: item['id'] == finder, self.books))

    def deleteById(self, id):
        self.books = list(filter(lambda item: item['id'] != id, self.books))
        return "Correctamente Eliminado"

    def saveBook(self, db: str) -> str:

        try:

            with open(db, "w") as file:

                titleItem = self.books[0]
                
                file.write(dictToStrLine(titleItem, True, self.__SEP))

                for book in self.books:

                    file.write(dictToStrLine(book, False, self.__SEP))
                    
        except Exception as error:
            print(error)
            exit()
        else:
            return "Correctamente guardado"
    