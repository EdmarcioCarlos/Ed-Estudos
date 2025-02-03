# Operados de comparação

"""
== igualdade
!= diferente
> maior | >= menor ou igual
< menor | <= menor ou igual

Condições
if
else
elif
"""

Idade = int(input('Digite a idade: '))

if Idade <18:
    print('Menor de idade')
elif Idade >=18 and Idade<60:
    print('Maior de idade')
else:
    print('Idoso')

  