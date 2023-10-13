textoArquivo = ""
with open("textoSituacoes.txt", "r", encoding="utf=8") as arquivo:
    for linha in arquivo:
        textoArquivo += linha
    conjuntoSituacoes = textoArquivo.split("*@*")

for i in range(len(conjuntoSituacoes)):
    situacaoAtual = conjuntoSituacoes[i].strip()

    situacaoAtual = f"def s{i+1}():\n" + "\tprint('''" + situacaoAtual + "''')\n\n"

    if "vá para" or "Vá para" in situacaoAtual:
        situacaoAtual = situacaoAtual + f"\tescolha = int(input('Qual a sua escolha?'))\n\tif escolha == X:\n\t\tsX()\n\telif escolha == Y:\n\t\tsY()\n\n"

    conjuntoSituacoes[i] = situacaoAtual

with open("situacoes.txt", "w", encoding="utf-8") as arquivo:
    for i in conjuntoSituacoes:
        arquivo.write(i)

listaDEFs = []
listaNums = []

with open("situacoes.txt", "r", encoding="utf-8") as arquivo:
    nDEF = 1
    for i in arquivo:
        if f"def s{nDEF}" in i:
            listaDEFs.append(nDEF)
            nDEF += 1

for i in range(401):
    listaNums.append(i)

for i in listaNums:
    if i == 0:
        listaNums.remove(i)

index = -1
for i in listaNums:
    index += 1
    if i != listaDEFs[index]:
        print(f"{i} É DIFERENTE DE {listaDEFs[index]}")
    else:
        print(f"{i} É IGUAL A  {listaDEFs[index]}")
