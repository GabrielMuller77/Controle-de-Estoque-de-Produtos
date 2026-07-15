import json
def salvar(dados, arquivo="produtos.json"):
    with open(arquivo, 'w', encoding='utf-8') as arq:
        json.dump(dados, arq, indent = 4, ensure_ascii=False)


        
def carregar(arquivo="produtos.json"):
    try:
        with open(arquivo, 'r', encoding='utf-8') as arq:
            registro = json.load(arq)
            return registro
    except FileNotFoundError:
        return []