import sistema
import arquivo
import menus
def cadastrar(produtos):
     while True:
        controle = input("Deseja cadatrar um produto: [S/N] ").upper().strip()
        if controle == 'S':
            nome_produto = input("Nome do Produto: ").upper()
            estoque_produto = int(input("Estoque atual do produto: "))
            capacidade_produto = int(input("Qual é o espaço reservado no estoque para armazenar o produto: "))
            sistema.verificaçao(estoque_produto, capacidade_produto)
            produto = {"Nome": nome_produto, "Estoque": estoque_produto, "Capacidade": capacidade_produto, "MovAceitas": 0, "MovRecusadas": 0, "Ocupado": 0}
            produtos.append(produto)
            arquivo.salvar(produtos)
        elif controle == 'N':
            print("Iniciando o sistema de estoque.")
            break
     sistema.estoque(produtos)   


def listar(produtos):
    for indice, produto in enumerate(produtos, 1):
            produto['Ocupado'] =  (produto["Estoque"] / produto["Capacidade"]) * 100
            print(f"Indice: {indice}\n Nome: {produto['Nome']}\n Estoque: {produto['Estoque']}\n Capacidade: {produto['Capacidade']}\n Ocupação: {produto['Ocupado']:.2f}%")


def delete(produtos):
     listar(produtos)
     while True:
        indice = int(input("Qual produto deseja excluir: 0 para cancelar. ")) 
        if (indice-1) < len(produtos) and (indice-1) >= 0:
            if indice != 0:
                indice -= 1
                produtos.pop(indice)
            else:
                print("Operação cancelada com sucesso")
                break
        else:
            print("Indice não encontrado, tente novamente")

def atualizar(produtos):
     while True:
        escolha = menus.menu_atualizar()
        listar(produtos) 
        indice = int(input("Qual produto deseja atualizar: "))
        indice -= 1
        match escolha:
            case '1':
                novo_nome = input("Qual o novo nome do produto: ")
                produtos[indice]["Nome"] = novo_nome
                arquivo.salvar(produtos)
            case '2':
                try:
                    novo_estoque = int(input("Qual o novo valor estocado: "))
                    produtos[indice]['Estoque'] = novo_estoque
                    arquivo.salvar(produtos)
                except ValueError:
                    print("Por favor digite um número válido")
            case '3':
                try:
                    nova_capacidade = int(input("Qual é a nova capacidade estabelecida: "))
                    produtos[indice]['Capacidade'] = nova_capacidade
                    arquivo.salvar(produtos)
                except ValueError:
                    print("Por favor digite um número válido")
            case '4':
                print("Saindo...")
                break
                
