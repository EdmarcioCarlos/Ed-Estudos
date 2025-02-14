"""
Enviar um e-mail com os detalhes da compra online (Maximo 3 tentativas para compras comfirmadas)
"""

Compra_Confirmada = False

Produto = str(input("Qual foi o produto comprado? "))
Valor = float(input("Qual o valor do produto? "))
Confirmar = str(input("Confirma a compra ?  S (SIM) / N (NÃO)"))

if Confirmar == "sim":
    Compra_Confirmada = True
else:
    Compra_Confirmada = False

for enviar in range(3):
    if Compra_Confirmada:
        print(f'O seu produto: {Produto} , foi confirmada a compra no valor de R$ {Valor}, detalhes serão enviados para seu e-mail')
        break
else: 
    print("!!! COMPRA NÃO VALIDADA!!!")