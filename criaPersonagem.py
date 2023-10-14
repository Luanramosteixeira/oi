import json
import jogardados
import personagem
def player():
    char = personagem.data
    player = dict()
    for i in range(len(char)):
        match i:
            case 0: player["habilidade"] = jogardados.habilidadeESorte()
            case 1: player ["energia"] = jogardados.energia()
            case 2: player["sorte"] = jogardados.habilidadeESorte()
            case 3: player['provisoes'] = 10
    print(f"Habilidade: {player['habilidade']}")
    print(f"Energia: {player['energia']}")
    print(f"Sorte: {player['sorte']}")
    print(f"Provisões: {player['provisoes']}")
    with open("player.json", "w") as file:
        file.write(json.dumps(player))

