import sorte

def s1():
    print("\nO clamor dos espectadores excitados some gradualmente atrás de você, que se aventura cada vez mais fundo na penumbra do túnel da caverna.\n")
    continuar = input("\nDigite qualquer tecla para continuar\n")
    print("\nGrandes cristais pendem do teto do túnel a intervalos de 20 metros, irradiando uma luz suave, apenas suficiente para que se veja por onde anda. À medida que seus olhos vão pouco a pouco se acostumando à quase escuridão, você começa a ver movimentos à sua volta. Aranhas e besouros sobem e descem pelas paredes entalhadas, desaparecendo em frestas e gretas ao sentir sua aproximação; ratazanas e ratos correm pelo chão à sua frente. Pingos de água caem em pequenas poças com um sinistro som gotejante que ecoa pelo túnel. O ar é frio, úmido e pesado. Depois de caminhar lentamente pelo túnel por uns cinco minutos, você chega a uma mesa de pedra encostada contra a parede à sua esquerda. Nela há seis caixas, uma das quais tem o seu nome pintado na tampa. Se você quiser abrir a caixa, digite 270. Se preferir continuar caminhando para o norte, digite 66.\n")
    escolha = int(input("Qual a sua escolha?\n"))
    if escolha == 270:
        s270()
    elif escolha == 66:
        s66()

def s2():
    print("\nO Escorpião consegue prendê-lo nas garras por tempo suficiente para mover a cauda segmentada para frente, por sobre a cabeça, e cravar em você o ferrão venenoso. O efeito é fatal, e você desaba no chão da Arena da Morte, imaginando se Throm conseguirá vencer.\n")

def s3():
    print("\nO Gnomo sacode a cabeça e diz: ‘Temo que você não tenha passado pela Prova dos Campeões. Os segredos do Calabouço da Morte do Barão Sukumvit ficarão guardados por mais um ano, pois você não terá permissão para sair daqui. Você foi indicado para ser meu servo pelo resto dos seus dias; preparará e modificará o subterrâneo para competidores futuros. Talvez em outra vida você tenha sucesso...’\n")

def s4():
    print("\nNa escuridão total, você não vê a curva do cano para baixo. Escorrega e, incapaz de se segurar no cano cheio de limo, desliza pela borda. Seus gritos ecoam pelo tubo, enquanto você cai 50 metros até o fundo. Você fracassou na Prova dos Campeões.\n")

def s5():
    print("\nVocê se arrasta pelo chão e se vê no covil de uma tribo de TROGLODITAS. Ao engatinhar passando por eles, sua bainha bate em uma pedra. Teste sua Sorte. Se você tiver sorte, vá para 185. Se você não tiver sorte, vá para 395.\n")
    testarSorte = input("Digite qualquer tecla para testar sua sorte: ")
    
    if sorte.usarSorte() == True:
        s185()
    else:
        s395()

def s6():
    print("\nSabendo que o Mantécora disparará os espinhos da cauda, Você corre para se proteger atrás de um dos pilares. Antes que consiga chegar lá, uma saraivada de espinhos voa pelo ar, e um deles penetra-lhe o braço. Você perde 2 pontos de ENERGIA. Se ainda estiver vivo, não perca tempo e ataque o Mantécora com espada, antes que ele possa disparar mais espinhos.\n")
    
def s7():
    print("\nAntes que você tenha tempo de chegar a uma porta, o rochedo já está sobre você, que grita de dor e medo quando ele o esmaga no chão. Sua aventura termina aqui.\n")

def s8():
    print("\nO Demônio do Espelho agarra-o pelo pulso. Imediatamente, ele começa a puxá-lo na direção do espelho. A força dele é incrível, e, apesar de todos os seus esforços, você não consegue evitar que o arraste progressivamente na direção do espelho. Quando ele toca o espelho, parece desaparecer diretamente através dele. Horrorizado, você vê seu próprio braço desaparecer, seguido pelo resto do corpo. Você está agora em um mundo de espelhos de outra dimensão, do qual jamais retornará.\n")

def s9():
    print("\nOs Hobgoblins não têm nada que lhe seja útil, por isso você resolve abrir o saco no chão. Dentro, acha uma moringa de barro arrolhada. Você a desarrolha e cheira o líquido que contém. O odor é penetrante e acre. Se quiser beber um pouco do líquido, vá para 158. Se quiser mergulhar um pedaço de pano nele, vá para 375.\n")
    escolha = int(input("Qual a sua escolha?\n"))
    if escolha == 158:
        s158()
    elif escolha == 375:
        s375()

def 10():
    