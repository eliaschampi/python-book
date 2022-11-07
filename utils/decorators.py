from termcolor import colored


def listToDict(title: list, row: list) -> dict:
    book = {}
    for count, value in enumerate(title):
        book[f"{value.strip()}"] = f"{row[count].strip()}"
    return book


def printAsTableForm(books: list):

    keys = books[0].keys()
    cols = "{:<17}" * len(keys)

    # show titles
    titles = iter(keys)
    print(colored(cols.format(*titles), "blue"))

    # show content
    for book in books:
        row = iter(book.values())
        print(cols.format(*row))

