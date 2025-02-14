"""
While loop
Cria um prmoção para um produto no valor de 5000
o mesmo deve reduzir seu valor ate um limite de custo
"""

Valor = 5000
Dia = 1
while Valor > 1000:
    Valor -= 1000
    Dia +=1
    print(f'No dia: {Dia} o valor do produto e : R$ {Valor}')