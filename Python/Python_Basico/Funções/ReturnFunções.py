''' (Dicas / tarefas)
Conceito de modulo seria o memso que Objeto em C#

Library > Packge > Module > Function

As fuções sempre devem estar no incio do codigo
'''


def Soma(*numero):
    resultado = 0
    for num in numero:
        resultado += num
    return resultado

x = Soma(100,500,300,400)
print(x)

