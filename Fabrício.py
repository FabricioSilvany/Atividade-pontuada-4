import os

os.system("cls || clear")

cardapio = []

pratos = input("Digite o número do prato desejado: ")
cardapio.append(pratos)

while True:
    match(pratos):
        case "1":
            print("Picanha: R$25.00")
            break
        case "2":
            print("Lasanha: R$20.00")
            break
        case "3":
            print("Strogonoff: R$18.00")
            break
        case "4":
            print("Bife acebolado: R$15.00")
            break
        case "5":
            print("Pão com ovo: R$5.00")
            break
        case "6":
            print("Feijoada: R$25.00")
            break
        case "7":
            print("Pirão de aipim: 20.00")
        case "0":
            break
        case _:
            print("Opção inválida\nTente novamente.")
    
    adicionando = input("Quer adicionar outra opção?: ")
    match(adicionando):
        case "sim":
            print("")