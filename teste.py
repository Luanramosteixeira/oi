textoArquivo = ""
with open("textoTeste.txt", "r", encoding="utf=8") as arquivo:
    for linha in arquivo:
        textoArquivo += linha
    conjuntoSituacoes = textoArquivo.split("*@*")
print(conjuntoSituacoes)