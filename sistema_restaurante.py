"""
Informe o número da turma: 
Turma - G93313

Nome completo dos componentes.
1 - Fabricio Silvany de Jesus
2 - Jonatas Fernandes dos Santos
3 - José Elias Lima Pereira
"""


import os

# Limpa o terminal.
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

print("""
         MENU

1 - picanha R$ 25,00
2 - lasanha R$ 20,00
3 - strogonoff R$ 18,00
4 - bife acebolado R$ 15,00
5 - pao com ovo R$ 5,00
6 - feijoada R$ 25,00
7 - pirao de aipim R$ 20,00
""")


