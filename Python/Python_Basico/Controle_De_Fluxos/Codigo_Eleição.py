"""
Criar um promaga para validar a idade minima para votar 
16 e o minimo para votar
"""

Idade = int(input("Digite sua Idade: "))

Resultado = 'Voto permitido' if Idade >= 16 else "Voto não permitido"
print(Resultado)