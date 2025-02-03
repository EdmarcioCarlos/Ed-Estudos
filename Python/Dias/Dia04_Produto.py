import math
#Criação de uma sistema de cadastro de produtos com aumento.


#Captura de dados
Valor_produto = float(input('Digite o valor do produto: R$ '))
Porcentagem_Aumento = int(input('Digite quanto deve ser aumentado o valor: '))

#Calculos
Novo_Valor = (Valor_produto * Porcentagem_Aumento)/100 + Valor_produto


#Exibir
print('---------------------------------')
print(f"O valor do produto e: R$ {Valor_produto:.2f} o valor final com acrecido de {Porcentagem_Aumento} % sera o valor de: R$ {Novo_Valor:.2f} ")
print('---------------------------------')