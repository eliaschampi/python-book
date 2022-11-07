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

elif chooseOption == "3":
    print("Estas son las habilidades de los pokemones: ")
    def pokemon_abilities(url_abil = 'https://pokeapi.co/api/v2/ability/', offset = 0):
        args = {'offset' : offset} if offset else {}

        response_abil = requests.get(url_abil, params=args)
        if response_abil.status_code == 200:
            payload_abil = response_abil.json()
            results_abil = payload_abil.get('results', [])

            if results_abil:
                for pokemon_abil in results_abil:
                    name_abil = pokemon_abil['name']
                    print(name_abil)
            #AGREGAR UN IF PARA TRAER LOS POKEMS DE CIERTAS HABILIDADES
            next_abilities = input("Continuar listando? [Y/N]: ").lower()
            if next_abilities == "y":
                pokemon_abilities(offset=offset+20)

            else:
                pokemon_abilities = int(input("Ingresa una de las habilidades para mostrar los pokemons con dicha habilidad(1,2,3,...327): "))

                def results_abilities(numabilities):
                    url_results_abilities = "https://pokeapi.co/api/v2/pokemon-habitat/" + str(numabilities)
                    response_results_abilities = requests.get(url_results_abilities)


                    if response_results_abilities.status_code == 200:

                        payload_results_abilities = response_results_abilities.json()
                        pokemon_results_abilities = payload_results_abilities.get('results', [])
                        
                        if pokemon_results_abilities:
                            for pokemon_results_abilities in pokemon_results_abilities:
                                name_results_abilities = pokemon_results_abilities['name']
                                print(name_results_abilities)
                       
                results_abilities(pokemon_abilities) 


    if __name__ == '__main__':
        url_abil = "https://pokeapi.co/api/v2/ability/" 
        pokemon_abilities()

elif chooseOption == "4":

    input_habit = int(input(colored("Qué habitat de pokemons quieres ver (1,2,3,4,5,6,7,8)?: ", "blue")))
    while input_habit not in (1, 2, 3, 4, 5,6,7,8):
        input_habit = int(input(colored("Qué habitat de pokemons quieres ver (0,1,2,3,4,5,6,7,8 )?: ", "blue")))

    def results_habitats(numHabit):
        url_results_habitats = "https://pokeapi.co/api/v2/pokemon-habitat/"
        response_results_habitats = requests.get(url_results_habitats)


        if response_results_habitats.status_code == 200:

            payload_results_habitats = response_results_habitats.json()
            pokemon_results_habitats = payload_results_habitats.get('results', [])
            print(pokemon_results_habitats[numHabit])
     
    results_habitats(input_habit)       

    def habitats(numGen):
        if __name__ == '__main__':
            url_gen = "https://pokeapi.co/api/v2/pokemon-habitat/" + str(numGen)

        response_habit = requests.get(url_gen)
        

        if response_habit.status_code == 200:

            payload_gen = response_habit.json()
            pokemon_species = payload_gen.get('pokemon_species', [])
        

            if pokemon_species:
                for pokemon_gen in pokemon_species:
                    name_gen = pokemon_gen['name']
                    print(name_gen)

    habitats(input_habit)

elif chooseOption == "5":
    print("Has elegido por tipo")
    input_type = input(colored("Qué tipo de pokemons quieres ver (1,2,3,4,...,20)?: ", "blue"))
    while input_type not in ("1", "2", "3", "4", "5","6","7","8","9"):
        input_type = input(colored("Qué tipo de pokemons quieres ver (1,2,3,4,...,20)?: ", "blue"))

    def types(numGen):
        url_type = "https://pokeapi.co/api/v2/type/" + numGen

        response_type = requests.get(url_type)
        if response_type.status_code == 200:
            payload_type = response_type.json()
            
            pokes = payload_type.get('pokemon', [])
            for pokemon_typ in pokes:
                name_type = pokemon_typ['pokemon']['name']
                print(name_type)

    types(input_type)

else:
    print("Elige una de las 5 opciones")