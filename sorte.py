import random

def usar_sorte(sorte_jogador):
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)

    if (dado1 + dado2) <= sorte_jogador:
        print("Você teve SORTE.")
        teve_sorte = True
    else:
        print("Você teve AZAR.")
        teve_sorte = False
    
    return teve_sorte
