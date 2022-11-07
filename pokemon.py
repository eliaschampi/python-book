from termcolor import colored
import requests

print(colored("\nBienvenido al mundo pokemon\n","blue"))

print(colored("Opción 1: Listar pokemons por generación","magenta"))
print(colored("Opción 2: Listar pokemons por forma","magenta"))
print(colored("Opción 3: Listar pokemons por habilidad","magenta"))
print(colored("Opción 4: Listar pokemons por habitat","magenta"))
print(colored("Opción 5: Listar pokemons por tipo","magenta"))

chooseOption = input("\nElige una de las opciones(1,2,3,4,5): ")
while chooseOption not in ("1", "2", "3", "4", "5"):
    chooseOption = input("\nElige una de las opciones(1,2,3,4,5): ")


if chooseOption == "1":
    input_gen = input(colored("Qué generación de pokemons quieres ver (1,2,3,4,5,6,7 u 8)?: ", "blue"))
    while input_gen not in ("1", "2", "3", "4", "5","6","7","8"):
        input_gen = input(colored("Qué generación de pokemons quieres ver (1,2,3,4,5,6,7 u 8)?: ", "blue"))

    def generations(numGen):
        if __name__ == '__main__':
            url_gen = "https://pokeapi.co/api/v2/generation/" + numGen

        response_gen = requests.get(url_gen)
        if response_gen.status_code == 200:
            payload_gen = response_gen.json()
            pokemon_species = payload_gen.get('pokemon_species', [])

            if pokemon_species:
                for pokemon_gen in pokemon_species:
                    name_gen = pokemon_gen['name']
                    print(name_gen)

    generations(input_gen)


elif chooseOption == "2":
    print("Has elegido las formas")



elif chooseOption == "5":
    print("Has elegido por tipo")
    print("Has elegido por tipo ")
    input_type = input(colored("Qué tipo de pokemons quieres ver (1,2,3,4,...,20)?: ", "blue"))
    while input_type not in ("1", "2", "3", "4", "5","6","7","8","9"):
        input_type = input(colored("Qué tipo de pokemons quieres ver (1,2,3,4,...,20)?: ", "blue"))

    def types(numGen):
        if __name__ == '__main__':
            url_type = "https://pokeapi.co/api/v2/type/" + numGen

        response_type = requests.get(url_type)
        if response_type.status_code == 200:
            payload_type = response_type.json()
            pokemon_type = payload_type.get('results', [])

            if pokemon_type:
                for pokemon_typ in pokemon_type:
                    name_type = pokemon_typ['name']
                    print(name_type)

    types(input_type)

else:
    print("Elige una de las 5 opciones")