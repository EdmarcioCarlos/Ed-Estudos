#region (Atividade- 1)
"""
Criar programa para controle de temperatuda
Menor que 10c - Muito frio
Menor que 20c - Esta fresco
O restante - Esta quente
"""
#endregion

Temperatura = float(input('Digite a temperatura atual da sua região: '))

if Temperatura <10:
    print(f'Sua região esta Muito fria! {Temperatura} c°')
elif Temperatura<20:
    print(f'Esta fresco na sua região! {Temperatura} c°')
else:
    print(f'Esta muito quenta na sua região!!! {Temperatura} c°')

