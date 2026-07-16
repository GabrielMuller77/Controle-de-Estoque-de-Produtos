def verificaçao(estoque_produto, capacidade_produto):
    if estoque_produto < 0:
        print("Não é possível informar um estoque negativo")
    elif estoque_produto > capacidade_produto:
        print("Estoque acima da capacidade máxima.")
    elif capacidade_produto <= 0:
        print("Não existe capacidade nula ou negativa em um estoque.")
    else:
       return True
