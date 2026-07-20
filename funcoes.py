def atualizar_ocupacao(produto):
    produto["Ocupado"] = produto["Estoque"] / produto["Capacidade"] * 100
    return produto["Ocupado"]
    