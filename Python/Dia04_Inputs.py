
#Captura de dados (MULTIPLOS)

Dados = input('Digite seu nome e idade e altura: ').split()
Nome = Dados[0]
Idade = int(Dados[1])
Altura = float(Dados[2])

#Exibir
print('---------------------------------')
#semple que usar o Upper lembre de colocar o ().
print(f"Seu nome e: {Nome.upper()} e você tem {Idade} anos e você tem {Altura} de altura !")
print('---------------------------------')