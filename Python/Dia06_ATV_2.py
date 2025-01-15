#region (Atividade- 2)
"""
Criar programa para controle de saudação
Bom dia - antes das 12pm
Boa tarde antes das 18:00
Boa noite - Restante
"""
#endregion

Horas = float(input('Digite quantas horas no momento: '))

if Horas <12:
    print(f'Bom dias! São {Horas:.2f} AM')
elif Horas<18:
    print(f'Boa tarde! São {Horas:.2f} PM')
else:
    print(f'Boa noite! São {Horas:.2f} PM')

