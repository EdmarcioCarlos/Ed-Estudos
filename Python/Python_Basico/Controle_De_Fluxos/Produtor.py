'''
Publicar um produto com comissão de 10% se for acima de R$200
'''

Nome_Produto = str(input('Digite o nome do produto: '))
Valor_produto = float(input('Digite o valor do seu produto: '))


while Valor_produto > 200:
    Valor_produto = (Valor_produto*0.10)+Valor_produto
    print(f'O valor final do produto: {Nome_Produto} e de: R${Valor_produto}')
    break