import os

os.system("cls || clear")

# Defs para o pagamento

def vista (valor_pratos):
    #Pagamento a vista recebe 10% de desconto
    valor_final = valor_pratos - (0.10 * valor_pratos)
    valor_descontado = (0.10 * valor_pratos)
    return valor_final, valor_descontado

def cartao (valor_pratos):
    #pagamento com cartão recebe 10% 
    valor_final = valor_pratos + (0.10 * valor_pratos)
    valor_adicionado = (0.10 * valor_pratos)
    return valor_final, valor_adicionado

