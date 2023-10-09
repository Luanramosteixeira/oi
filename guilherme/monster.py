import characters
import json
import dice

def createMonster(hability, sort):
    char = [characters.data[0], characters.data[1], "Ataque"]
    monster = dict()
    with open("db/monster/monster.json", "r") as file:
        monster = json.loads(file.read())
    for i in range(len(char)):
        match i:
            case 0: monster['hability'] = hability
            case 1: monster['energy'] = sort
            case 2: monster['atack'] = dice.sort()
    with open("db/monster/monster.json", "w") as file:
        file.write(json.dumps(monster))