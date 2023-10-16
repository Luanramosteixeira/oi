import json
def atualizar_inventario(modificacoes):
    # Primeiro, carregue o inventário atual do arquivo JSON (se existir).
    try:
        with open("inventario.json", "r", encoding='utf-8') as arquivo:
            inventario = json.loads(arquivo.read())
    except FileNotFoundError:
        # Se o arquivo não existe, crie um inventário vazio.
        inventario = {
            "equipamentos": [],
            "ouro": 0,
            "joias": 0,
            "pocoes": 0
        }

    # Atualize o inventário com as modificações fornecidas.
    for chave, valor in modificacoes.items():
        if chave == "equipamentos":
            if isinstance(valor, str):
                inventario[chave].append(valor)
        elif chave in inventario:
            inventario[chave] += valor

    # Salve o inventário atualizado de volta no arquivo JSON.
    with open("inventario.json", "w", encoding='utf-8') as arquivo:
        arquivo.write(json.dumps(inventario))

    return inventario

def adicionar_monstro(nome, habilidade, energia):
    # Primeiro, carregue a lista de monstros atual do arquivo JSON (se existir).
    try:
        with open("monstros.json", "r", encoding='utf-8') as arquivo:
            monstros = json.loads(arquivo.read())
    except FileNotFoundError:
        # Se o arquivo não existe, crie uma lista vazia de monstros.
        monstros = []

    # Crie um dicionário representando o novo monstro.
    novo_monstro = {
        'nome': nome,
        'habilidade': habilidade,
        'energia': energia
    }

    # Adicione o novo monstro à lista de monstros.
    monstros.append(novo_monstro)

    # Salve a lista de monstros atualizada de volta no arquivo JSON.
    with open("monstros.json", "w", encoding='utf-8') as arquivo:
        arquivo.write(json.dumps(monstros))

    print(f"Monstro '{nome}' adicionado com sucesso!")