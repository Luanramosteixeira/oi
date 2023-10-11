import random

sorte = 3

def usar_sorte(sorte_jogador):
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)

    if (dado1 + dado2) <= sorte_jogador:
        print("Você teve sorte.")
    else:
        print("Você está com azar.")
    
    sorte_jogador -= 1
    return sorte_jogador
