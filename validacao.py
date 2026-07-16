def verificaçao(estoque_produto, capacidade_produto):
    if estoque_produto < 0:
        print("Não é possível informar um estoque negativo")
        return False
    elif estoque_produto > capacidade_produto:
        print("Estoque acima da capacidade máxima.")
        return False
    elif capacidade_produto <= 0:
        print("Não existe capacidade nula ou negativa em um estoque.")
        return False
    else:
       return True
    

def validar_indice(indice,  produtos):
    if (indice-1) < len(produtos) and (indice-1) >= 0:
        indice -= 1
        return indice
    else:
        return None
