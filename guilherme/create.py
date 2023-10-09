import json
import dice
import characters

def player():
    char = characters.data
    player = dict()
    with open("db/player/player.json", "r") as file:
        player = json.loads(file.read())
    for i in range(len(char)):
        match i:
            case 0: player['hability'] = dice.sort()
            case 1: player ['energy'] = dice.sort()
            case 2: player['lucky'] = dice.sort()
            case 3: player['provision'] = dice.sort()
    print(f"Habilidade: {player['hability']}")
    print(f"Energia: {player['energy']}")
    print(f"Sorte: {player['lucky']}")
    print(f"Sorte: {player['lucky']}")
    print(f"Provisões: {player['provision']}")
    with open("db/player/player.json", "w") as file:
        file.write(json.dumps(player))

def monster(hability, sort):
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