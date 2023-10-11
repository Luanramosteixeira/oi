import random
import sorte

def combate(sorte_jog, habilidade_jog, energia_jog, habilidade_cri, energia_cri, fuga):
    n_rodada = 0
    while not (energia_jog == 0 or energia_cri == 0):
        n_rodada += 1
        print(f"RODADA {n_rodada}\n")
        print(f"ENERGIA DO JOGADOR: {energia_jog}")
        print(f"ENERGIA DA CRIATURA: {energia_cri}")
        jogar_dados = input(f"\nJogue os dados para a criatura (Digite J): ")
        if jogar_dados.lower() == "j":
            dado1 = random.randint(1, 6)
            dado2 = random.randint(1, 6)

            forca_ataque_criatura = (dado1+dado2) + habilidade_cri
            print(f"\nA força de ataque da CRIATURA é de {forca_ataque_criatura} pontos.\n")

        jogar_dados = input(f"Jogue os dados para você (Digite J): ")
        if jogar_dados.lower() == "j":
            dado1 = random.randint(1, 6)
            dado2 = random.randint(1, 6)

            forca_ataque_jogador = (dado1+dado2) + habilidade_jog
            print(f"\nA SUA força de ataque é de {forca_ataque_jogador} pontos.\n")
        
        if forca_ataque_jogador > forca_ataque_criatura:
            print("Você acertou a criatura!")
            energia_cri -= 2
            sorte_opcao = input("Você deseja usar a sorte? (S/N)\n")
            if sorte_opcao.lower() == "s":
                sorte.usar_sorte(sorte_jog)

            print("-"*50)
        elif forca_ataque_jogador < forca_ataque_criatura:
            print("A criatura te acertou!")
            print("-"*50)
            energia_jog -= 2
        else:
            print("Ninguém se feriu!")
            print("-"*50)
            continue

        if energia_jog == 0:
            vencedor = "a criatura"
        elif energia_cri == 0:
            vencedor = "o jogador"
    print(f"O vencedor deste combate foi {vencedor.upper()}.")
