import crud
import arquivo
import menus
def main():
    lista_produtos = arquivo.carregar()
    while True:
        menu = menus.menu_principal()
        match menu:
            case '1':
                crud.cadastrar(lista_produtos)
            case '2':
                crud.listar(lista_produtos)
            case '3':
                crud.atualizar(lista_produtos)
            case '4':
                crud.delete(lista_produtos)
            case '5':
                crud.movimentar(lista_produtos)
            case '6':
                print("Encerrando sistema...")
                break
            case _:
                print("Escolhan inválida, tente novamente mais tarde.")
    


if __name__ == '__main__':
    main()