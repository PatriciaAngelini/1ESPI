#Exercicio
#Listar o nome dos herois que tem o super poder de voar
#Flight
import json
heroes_flight = {}
with open('heroes.json', 'r', encoding='utf-8') as aHero:
    heroes = json.load(aHero)
    print(type(heroes))
    for member in heroes['members']:
        print(member)
        if 'Flight' in member['powers']:
            print(member['name'])
            heroes_flight.update({member['name']:member['powers']})
    print(heroes_flight)

# e agora, se quisessemos gravar um arquivo json separado
# so com os herois que voam
with open('heroes_flight.json', 'w', encoding='utf-8') as aFlight:
    json.dump(heroes_flight, aFlight, indent=4,ensure_ascii=False)