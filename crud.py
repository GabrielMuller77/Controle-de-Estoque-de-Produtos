import validacao
import arquivo
import menus
import funcoes
def cadastrar(produtos):
     while True:
        nome_produto = input("Nome do Produto: ").upper()
        estoque_produto = validacao.validar_int("Estoque atual do produto: ")
        capacidade_produto = validacao.validar_int("Qual é o espaço reservado no estoque para armazenar o produto: ")
        if validacao.verificacao(estoque_produto, capacidade_produto):
            produto = {"Nome": nome_produto, "Estoque": estoque_produto, "Capacidade": capacidade_produto, "MovAceitas": 0, "MovRecusadas": 0, "Ocupado": 0}
            funcoes.atualizar_ocupacao(produto)
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
        


def listar(produtos):
    for indice, produto in enumerate(produtos, 1):
            print(f"Indice: {indice}\n Nome: {produto['Nome']}\n Estoque: {produto['Estoque']}\n Capacidade: {produto['Capacidade']}\n Ocupação: {produto['Ocupado']:.2f}%")


def delete(produtos):
     listar(produtos)
     while True:
        indice = validacao.validar_int("Qual produto deseja excluir: 999 para cancelar. ")
        if indice == 999:
            print("Saindo...")
            break
        else:
            indice_valido = validacao.validar_indice(indice, produtos)
            if indice_valido is None:
                print("Índice não encontrado, tente novamente")
                continue
            print(f"Produto {produtos[indice_valido]["Nome"]} excluído com sucesso.")
            produtos.pop(indice_valido)
            arquivo.salvar(produtos)

def atualizar(produtos):
    while True:
        escolha = menus.menu_atualizar() 
        if escolha == '4':
            print("Saindo...")
            break
        listar(produtos) 
        indice = validacao.validar_int("Qual produto deseja atualizar: ")
        indice_valido = validacao.validar_indice(indice, produtos)
        if indice_valido is None:
            print('Índice inexistente, tente novamente')
            continue
        produto = produtos[indice_valido]
        match escolha:
            case '1':
                novo_nome = input("Qual o novo nome do produto: ")
                produto["Nome"] = novo_nome
            case '2':
                novo_estoque = validacao.validar_int("Qual o novo valor estocado: ")
                if validacao.verificacao(novo_estoque, produto["Capacidade"]):
                    produto['Estoque'] = novo_estoque
                    funcoes.atualizar_ocupacao(produto)
            case '3':
                    nova_capacidade = validacao.validar_int("Qual é a nova capacidade estabelecida: ")
                    if validacao.verificacao(produto["Estoque"], nova_capacidade):
                        produto['Capacidade'] = nova_capacidade
                        funcoes.atualizar_ocupacao(produto)
            case _:
                print("Opção inválida")
        arquivo.salvar(produtos)

def movimentar(produtos):
    while True:
        listar(produtos)
        controle_estoque = validacao.validar_int("Qual operação deseja executar, 0 para encerrar: ")
        if controle_estoque == 0:
            arquivo.salvar(produtos)
            for produto in produtos:
                print(f"Nome: {produto['Nome']}\n Estoque: {produto['Estoque']}\n Capacidade: {produto['Capacidade']}\n Movimentações aceitas: {produto["MovAceitas"]}\n Movimentações recusadas: {produto['MovRecusadas']}\n Ocupação: {produto['Ocupado']:.2f}%")
            print("Programa encerrado")
            break
        indice = validacao.validar_int("Qual o índice do produto que deseja alterar: ")
        indice_valido = validacao.validar_indice(indice, produtos)
        if indice_valido is None:
            print('Índice inválido, tente novamente')
            continue
        produto = produtos[indice_valido]
        if controle_estoque > 0:
            if produto["Estoque"] + controle_estoque > produto["Capacidade"]:
                produto["MovRecusadas"] += 1
                print("O estoque não possui armazenamento necessário para adicionar os itens.")
            else:
<<<<<<< Updated upstream
                print('Índice inválido, tente novamente')
                continue
                    
=======
                produto["MovAceitas"] += 1
                produto["Estoque"] += controle_estoque
                funcoes.atualizar_ocupacao(produto)
                print(f"{controle_estoque} itens adicionados com sucesso ao estoque, estoque atual do produto: {produto["Estoque"]}")
        else:
            if abs(controle_estoque) > produto["Estoque"]:
                produto["MovRecusadas"] += 1
                print("Não há estoque suficiente para efetuar a ação.")
            else:
                produto["MovAceitas"] += 1 
                produto["Estoque"] += controle_estoque
                funcoes.atualizar_ocupacao(produto)
                print(f"{abs(controle_estoque)} itens retirados com sucesso ao estoque, estoque atual do produto: {produto["Estoque"]}")
        arquivo.salvar(produtos)
            
>>>>>>> Stashed changes
