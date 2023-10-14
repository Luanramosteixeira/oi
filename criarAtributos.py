import random

def habilidade(): 
    dado1 = random.randint(1, 6)
    return dado1 + 6

def energia(): 
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return (dado1 + dado2) + 12

def sorte(): 
    dado1 = random.randint(1, 6)
    return dado1 + 6