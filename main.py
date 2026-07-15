import sistema
import arquivo
def main():
    lista_produtos = arquivo.carregar()
    while True:
        controle = input("Deseja cadatrar um produto: [S/N] ").upper().strip()
        if controle == 'S':
            nome_produto = input("Nome do Produto: ").upper()
            estoque_produto = int(input("Estoque atual do produto: "))
            capacidade_produto = int(input("Qual é o espaço reservado no estoque para armazenar o produto: "))
            sistema.verificaçao(estoque_produto, capacidade_produto)
            produto = {"Nome": nome_produto, "Estoque": estoque_produto, "Capacidade": capacidade_produto, "MovAceitas": 0, "MovRecusadas": 0, "Ocupado": 0}
            lista_produtos.append(produto)
        elif controle == 'N':
            print("Iniciando o sistema de estoque.")
            break
    sistema.estoque(lista_produtos)       
    #estoque_inicial = int(input("Estoque inicial: "))
    #limite_estoque = int(input("Capacidade máxima do estoque: "))
    #if estoque_inicial < 0:
    #   print("Não é possível informar um estoque negativo")
    #elif estoque_inicial > limite_estoque:
    #    print("Estoque acima da capacidade máxima.")
    #elif limite_estoque <= 0:
    #    print("Não existe capacidade nula ou negativa em um estoque.")
    #else:
    #    sistema.estoque(estoque_inicial, limite_estoque, lista_produtos)


if __name__ == '__main__':
    main()