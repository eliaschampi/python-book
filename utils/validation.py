from utils import constants


def validateMenuOptions(options: list, userinput) -> None:

    counter = 0
    limit = constants.LIMIT_TRIES
    while userinput not in options and counter < limit:
        userinput = input("Ingresa una opción: => ")
        counter += 1
    else:
        if userinput in options:
            return userinput
        else:
            print(f"Ingresaste una opción incorrecta {counter} veces. Adios")
            exit()

def validateBookItem(bookItem: dict):

    id, Titulo, Genero, Editorial, Autor = bookItem.values()
    if not id:
        return "Campo id es obligatorio", False
    
    if not Titulo:
        return "Campo titulo es obligatorio", False
    
    if not Genero:
        return "Campo género es obligatorio", False

    if not Editorial:
        return "Campo editorial es obligatorio", False
    
    if not Autor:
        return "Campo autor es obligatorio", False
    
    return "Campos verificados", True

