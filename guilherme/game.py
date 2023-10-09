import create

def main():
    try:
        print("Olá, seja bem-vindo (a) ao Calabouso da morte")
        print("")
        quest = input("Deseja aceitar o desafio? (S/N) ").upper()
        while quest != "S" and quest != "N":
            quest = input("Deseja aceitar o desafio? (S/N) ").upper()
        if quest == "N":
            print("Okay, até mais!")
            raise KeyboardInterrupt
        divider()
        print("Sorteando o personagem...\n")
        create.player()
        divider()
    except KeyboardInterrupt:
        pass
    finally: 
        print("\nPrograma encerrado!")


def divider(): print("_"*100)

main()