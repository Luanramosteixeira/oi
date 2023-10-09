import json
import dice
import characters

def createPlayer():
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
    with open("db/player/player.json", "w") as file:
        file.write(json.dumps(player))