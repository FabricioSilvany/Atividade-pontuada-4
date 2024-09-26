"""
Informe o número da turma: 
Turma - G93313

Nome completo dos componentes.
1 - Fabricio Silvany de Jesus
2 - Jonatas Fernandes dos Santos
3 - José Elias Lima Pereira
4 - Victor Andrade Costa Pinto
"""


import os

# Limpa o terminal.
os.system("cls || clear") 

#Listas
pedidos_preco = []
pedidos_nomes = []

# def para o Menu
def menu():
    os.system("cls || clear") 
    print("""
    ======== MENU ========

    1 - picanha R$ 25,00
    2 - lasanha R$ 20,00
    3 - strogonoff R$ 18,00
    4 - bife acebolado R$ 15,00
    5 - pao com ovo R$ 5,00
    6 - feijoada R$ 25,00
    7 - pirao de aipim R$ 20,00
    """)



# Defs para o pagamento

def vista (valor_pratos):
    #Pagamento a vista recebe 10% de desconto
    valor_final = valor_pratos - (0.10 * valor_pratos)
    
    
    
    return valor_final

def desconto (valor_pratos):
    valor_descontado = (0.10 * valor_pratos)
    return  valor_descontado

def cartao (valor_pratos):
    #pagamento com cartão recebe 10% 
    valor_final = valor_pratos + (0.10 * valor_pratos)
    
    

    return valor_final

def acresimo (valor_pratos):
    valor_adicionado = (0.10 * valor_pratos)
    return valor_adicionado

menu()


while True:
    pratos = float(input("\nDigite o número do prato desejado: "))
    os.system("cls || clear")
    
    match(pratos):
        case 1:
            pedidos_preco.append(25)
            pedidos_nomes.append("1 - Picanha: R$25,00")

        case 2:
            pedidos_preco.append(20)
            pedidos_nomes.append("2 - Lasanha: R$20,00")
            
        case 3:
            pedidos_preco.append(18)
            pedidos_nomes.append("3 - Strogonoff: R$18,00")

        case 4:
            pedidos_preco.append(15)
            pedidos_nomes.append("4 - Bife acebolado: R$15,00")

        case 5:
            pedidos_preco.append(5)
            pedidos_nomes.append("5 - Pão com ovo: R$5,00")

        case 6:
            pedidos_preco.append(25)
            pedidos_nomes.append("6 - Feijoada: R$25,00")

        case 7:
            pedidos_preco.append(20)
            pedidos_nomes.append("7 - Pirão de aimpim: R$20,00")

        case 0:
            break

        case _:
            print("Opção inválida\nTente novamente.")
            
    adicionar_prato = input("\nQuer adicionar outro prato? \nSe quiser adicionar outro prato digite 'sim'\nSenão digite'0' \nR: ").lower()

    if adicionar_prato == "sim":
        menu()
    else:
        break

valor_pratos = sum(pedidos_preco)

        
pagamento = int(input("""
Digite sua forma de pagamento:
                                             
1 - À vista
2 - Cartão

R: """))

valor_pratos = sum(pedidos_preco)

match(pagamento):
    case 1:
        forma_pagamento = "À vista"
        valor_final = vista(valor_pratos)
        valor_descontado = desconto(valor_pratos)
        print("\nDesconto de 10%!")
        print(f"Valor descontado: R${valor_descontado}")
    case 2:
        forma_pagamento = "Cartão"
        valor_final = cartao(valor_pratos)
        valor_adicionado = acresimo(valor_pratos)
        print("Seu valor final teve um acrescimo de 10%!")
        print(f"Acrescimo de: R${valor_adicionado}")



for i, pedidos in enumerate(pedidos_nomes):
    print(f"{i+1}º pedido: {pedidos}")


print(f"\nValor dos pratos: {valor_pratos}")
print(f"\nForma de Pagamento: {forma_pagamento}")
print(f"\nValor final: {valor_final}")
