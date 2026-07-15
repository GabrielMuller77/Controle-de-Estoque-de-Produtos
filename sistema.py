import arquivo
def estoque(produtos):
   
    while True:
        for indice, produto in enumerate(produtos, 1):
            produto['Ocupado'] =  (produto["Estoque"] / produto["Capacidade"]) * 100
            print(f"Indice: {indice}\n Nome: {produto['Nome']}\n Estoque: {produto['Estoque']}\n Capacidade: {produto['Capacidade']}\n Ocupação: {produto['Ocupado']:.2f}%")
        controle_estoque = int(input("Qual operação deseja realizar: [0 para sair] "))
        if controle_estoque == 0:
            arquivo.salvar(produtos)
            for produto in produtos:
                print(f"Nome: {produto['Nome']}\n Estoque: {produto['Estoque']}\n Capacidade: {produto['Capacidade']}\n Movimentações aceitas: {produto["MovAceitas"]}\n Movimentações recusadas: {produto['MovRecusadas']}\n Ocupação: {produto['Ocupado']:.2f}%")
            print("Programa encerrado")
            break
        else:
            indice = int(input("Qual o índice do produto que deseja alterar: "))
            indice -= 1
            if controle_estoque > 0:
                if produtos[indice]["Estoque"] + controle_estoque > produtos[indice]["Capacidade"]:
                    produtos[indice]["MovRecusadas"] += 1
                    print("O estoque não possui armazenamento necessário para adicionar os itens.")
                else:
                    produtos[indice]["MovAceitas"] += 1
                    produtos[indice]["Estoque"] += controle_estoque
                    print(f"{controle_estoque} itens adicionados com sucesso ao estoque, estoque atual do produto: {produtos[indice]["Estoque"]}")
            else:
                if controle_estoque < 0:
                    if abs(controle_estoque) > produtos[indice]["Estoque"]:
                        produtos[indice]["MovRecusadas"] += 1
                        print("Não há estoque suficiente para efetuar a ação.")
                    else:
                        produtos[indice]["MovAceitas"] += 1 
                        produtos[indice]["Estoque"] += controle_estoque
                        print(f"{controle_estoque} itens retirados com sucesso ao estoque, estoque atual do produto: {produtos[indice]["Estoque"]}")
                

def verificaçao(estoque_produto, capacidade_produto):
    if estoque_produto < 0:
        print("Não é possível informar um estoque negativo")
    elif estoque_produto > capacidade_produto:
        print("Estoque acima da capacidade máxima.")
    elif capacidade_produto <= 0:
        print("Não existe capacidade nula ou negativa em um estoque.")
    else:
       return True
