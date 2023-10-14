import json
import criarAtributos

def criar():
    jogador = dict()
    with open("jogador.json", "r", encoding='utf-8') as arquivo:
        jogador = json.loads(arquivo.read())
    for i in range(4):
        match i:
            case 0: jogador['habilidade'] = criarAtributos.habilidade()
            case 1: jogador['energia'] = criarAtributos.energia()
            case 2: jogador['sorte'] = criarAtributos.sorte()
            case 3: jogador['provisões'] = 10
    print(f"Habilidade: {jogador['habilidade']}")
    print(f"Energia: {jogador['energia']}")
    print(f"Sorte: {jogador['sorte']}")
    print(f"Provisões: {jogador['provisões']}")
    with open("jogador.json", "w", encoding='utf-8') as arquivo:
        arquivo.write(json.dumps(jogador))

    return jogador
