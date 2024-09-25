import os

os.system("cls || clear")

pedidos_preco = []
pedidos_nomes = []

while True:
    pratos = float(input("\nDigite o número do prato desejado: "))
    os.system("cls || clear")
    
    match(pratos):
        case 1:
            pedidos_preco.append(25)
            pedidos_nomes.append("1- Picanha: R$25,00")

        case 2:
            pedidos_preco.append(20)
            pedidos_nomes.append("2- Lasanha: R$20,00")
            
        case 3:
            pedidos_preco.append(18)
            pedidos_nomes.append("3- Strogonoff: R$18,00")

        case 4:
            pedidos_preco.append(15)
            pedidos_nomes.append("4- Bife acebolado: R$15,00")

        case 5:
            pedidos_preco.append(5)
            pedidos_nomes.append("5- Pão com ovo: R$5,00")

        case 6:
            pedidos_preco.append(25)
            pedidos_nomes.append("6- Feijoada: R$25,00")

        case 7:
            pedidos_preco.append(20)
            pedidos_nomes.append("7- Pirão de aimpim R$20,00")

        case 0:
            break

        case _:
            print("Opção inválida\nTente novamente.")
            
    adicionar_prato = input("\nQuer adicionar outro prato? \nSe quiser adicionar outro prato digite 'sim'\nSenão digite'0' \nR: ").lower()
    os.system("cls ||")
    if adicionar_prato == "sim":
        ()
    else:
        break

for i, pedidos in enumerate(pedidos_nomes):
    print(f"{i+1}º pedido: {pedidos}")