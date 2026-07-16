import validacao
import arquivo
import menus
def cadastrar(produtos):
     while True:
        nome_produto = input("Nome do Produto: ").upper()
        estoque_produto = int(input("Estoque atual do produto: "))
        capacidade_produto = int(input("Qual é o espaço reservado no estoque para armazenar o produto: "))
        if validacao.verificaçao(estoque_produto, capacidade_produto):
            produto = {"Nome": nome_produto, "Estoque": estoque_produto, "Capacidade": capacidade_produto, "MovAceitas": 0, "MovRecusadas": 0, "Ocupado": 0}
            produto['Ocupado'] =  (produto["Estoque"] / produto["Capacidade"]) * 100
            produtos.append(produto)
            arquivo.salvar(produtos)
            controle = input("Deseja cadastrar mais produtos, S ou N: ").upper().strip()
            if controle == 'S':
                continue
            else:
                print("Saindo do cadastro")
                break
        else:
            print('Tente novamente')
            continue
        


def listar(produtos):
    for indice, produto in enumerate(produtos, 1):
            produto['Ocupado'] =  (produto["Estoque"] / produto["Capacidade"]) * 100
            print(f"Indice: {indice}\n Nome: {produto['Nome']}\n Estoque: {produto['Estoque']}\n Capacidade: {produto['Capacidade']}\n Ocupação: {produto['Ocupado']:.2f}%")


def delete(produtos):
     listar(produtos)
     while True:
        indice = int(input("Qual produto deseja excluir: 999 para cancelar. "))
        if indice == 999:
            print("Operação cancelada com sucesso")
            break
        else:
            indice_valido = validacao.validar_indice(indice, produtos)
            if indice_valido is not None:
                produtos.pop(indice_valido)
                arquivo.salvar(produtos)
            else:
                print("Indice não encontrado, tente novamente")
                continue

def atualizar(produtos):
    escolha = menus.menu_atualizar() 
    while True:
        listar(produtos) 
        indice = int(input("Qual produto deseja atualizar: "))
        indice_valido = validacao.validar_indice(indice, produtos)
        if indice_valido is not None:
            match escolha:
                case '1':
                    novo_nome = input("Qual o novo nome do produto: ")
                    produtos[indice_valido]["Nome"] = novo_nome
                    arquivo.salvar(produtos)
                case '2':
                    try:
                        novo_estoque = int(input("Qual o novo valor estocado: "))
                        produtos[indice_valido]['Estoque'] = novo_estoque
                        arquivo.salvar(produtos)
                    except ValueError:
                        print("Por favor digite um número válido")
                case '3':
                    try:
                        nova_capacidade = int(input("Qual é a nova capacidade estabelecida: "))
                        produtos[indice_valido]['Capacidade'] = nova_capacidade
                        arquivo.salvar(produtos)
                    except ValueError:
                        print("Por favor digite um número válido")
                case '4':
                    print("Saindo...")
                    break
        else:
            print('Índice inexistente, tente novamente')
            continue            

def movimentar(produtos):
    while True:
        listar(produtos)
        controle_estoque = int(input("Qual operação deseja executar, 0 para encerrar: "))
        if controle_estoque == 0:
            arquivo.salvar(produtos)
            for produto in produtos:
                print(f"Nome: {produto['Nome']}\n Estoque: {produto['Estoque']}\n Capacidade: {produto['Capacidade']}\n Movimentações aceitas: {produto["MovAceitas"]}\n Movimentações recusadas: {produto['MovRecusadas']}\n Ocupação: {produto['Ocupado']:.2f}%")
            print("Programa encerrado")
            break
        else:
            indice = int(input("Qual o índice do produto que deseja alterar: "))
            indice_valido = validacao.validar_indice(indice, produtos)
            if indice_valido is not None:
                if controle_estoque > 0:
                    if produtos[indice_valido]["Estoque"] + controle_estoque > produtos[indice_valido]["Capacidade"]:
                        produtos[indice_valido]["MovRecusadas"] += 1
                        print("O estoque não possui armazenamento necessário para adicionar os itens.")
                        arquivo.salvar(produtos)
                    else:
                        produtos[indice_valido]["MovAceitas"] += 1
                        produtos[indice_valido]["Estoque"] += controle_estoque
                        print(f"{controle_estoque} itens adicionados com sucesso ao estoque, estoque atual do produto: {produtos[indice_valido]["Estoque"]}")
                        arquivo.salvar(produtos)
                else:
                    if controle_estoque < 0:
                        if abs(controle_estoque) > produtos[indice_valido]["Estoque"]:
                            produtos[indice_valido]["MovRecusadas"] += 1
                            print("Não há estoque suficiente para efetuar a ação.")
                            arquivo.salvar(produtos)
                        else:
                            produtos[indice_valido]["MovAceitas"] += 1 
                            produtos[indice_valido]["Estoque"] += controle_estoque
                            print(f"{controle_estoque} itens retirados com sucesso ao estoque, estoque atual do produto: {produtos[indice_valido]["Estoque"]}")
                            arquivo.salvar(produtos)
            else:
                print('Índice inválido, tente novamente')
                continue
                    