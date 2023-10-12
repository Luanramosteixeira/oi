import random

def usarSorte(sorte_jogador):
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)

    if (dado1 + dado2) <= sorte_jogador:
        print("\nVocê teve SORTE.\n")
        teve_sorte = True
    else:
        print("\nVocê teve AZAR.\n")
        teve_sorte = False
    
    return teve_sorte
