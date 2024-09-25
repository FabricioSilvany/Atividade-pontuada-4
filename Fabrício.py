import os

os.system("cls || clear")


while True:
    pratos = int(input("\nDigite o número do prato desejado: "))
    os.system("cls || clear")
    
    match(pratos):
        case 1:
            print("\nPrato adicionado ao seu pedido")
            print("Picanha: R$25.00")

        case 2:
            print("\nPrato adicionado ao seu pedido")
            print("Lasanha: R$20.00")
            
        case 3:
            print("\nPrato adicionado ao seu pedido")
            print("Strogonoff: R$18.00")

            
        case 4:
            print("\nPrato adicionado ao seu pedido")
            print("Bife acebolado: R$15.00")

        case 5:
            print("\nPrato adicionado ao seu pedido")
            print("Pão com ovo: R$5.00")

        case 6:
            print("\nPrato adicionado ao seu pedido")
            print("Feijoada: R$25.00")

        case 7:
            print("\nPrato adicionado ao seu pedido")
            print("Pirão de aipim: 20.00")

        case 0:
            break

        case _:
            print("Opção inválida\nTente novamente.")