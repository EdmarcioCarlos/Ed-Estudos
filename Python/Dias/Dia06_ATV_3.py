#region (Atividade- 3)
"""
Criar programa para dar descontos
1 - Usurario deve digitar o valor da compra.
2 - Valor da compra < 100 desconto de 5%
3 - Valor da compra < 200 desconto de 10%
4 - Valor da compra > 200 desconto de 20%
"""
#endregion

Valor = float(input('Digite o valor da compra: '))
Desconto = 0
Valor_descontado=0

if Valor <100:
    Desconto = 5
    Valor_descontado = Valor-(Valor*Desconto)/100
    print(f'O valor da sua compra e: R$ {Valor:.2f} e lhe foi concedido o desconto de {Desconto}% que fica o valor de R$ {Valor_descontado:.2f}')
elif Valor <200:
    Desconto = 10
    Valor_descontado = Valor-(Valor*Desconto)/100
    print(f'O valor da sua compra e: R$ {Valor:.2f} e lhe foi concedido o desconto de {Desconto}% que fica o valor de R$ {Valor_descontado:.2f}')
else:
    Desconto = 20
    Valor_descontado = Valor-(Valor*Desconto)/100
    print(f'O valor da sua compra e: R$ {Valor:.2f} e lhe foi concedido o desconto de {Desconto}% que fica o valor de R$ {Valor_descontado:.2f}')
