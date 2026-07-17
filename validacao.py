def verificacao(estoque_produto, capacidade_produto):
    if capacidade_produto <= 0:
        print("Não existe capacidade nula ou negativa em um estoque.")
        return False
    if estoque_produto < 0:
        print("Não é possível informar um estoque negativo.")
        return False
    if estoque_produto > capacidade_produto:
        print("Estoque acima da capacidade máxima.")
        return False
    return True
    

def validar_indice(indice,  produtos):
    if (indice-1) < len(produtos) and (indice-1) >= 0:
        indice -= 1
        return indice
    else:
        return None
    

def validar_int(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Valor inválido, tente novamente")
            
    
