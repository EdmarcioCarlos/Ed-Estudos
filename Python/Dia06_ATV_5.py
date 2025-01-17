#region (Atividade- 5)
"""
Desempenho escolar

1 - Professor digita a nota

2 - Sistema calcula de acordo:
Nota > ou = a 9 EXELENTE NOTA A
Nota > ou = a 7 BOM TRABALHO NOTA B
Nota > ou = a 5 VOCE PASSOU MAS PRECISA MELHORA NOTA C
Nota < a 5 VOCE REPROVADO
"""
#endregion

Nota = float(input("Digite a nota do aluno: "))

if Nota>=9:
    print(f"EXELENTE NOTA A EM PONTOS FICOU: {Nota}")
elif Nota>=7:
    print("BOM TRABALHO NOTA B EM PONTOS FICOU: {Nota}")
elif Nota>=5:
    print("VOCE PASSOU MAS PRECISA MELHORA NOTA C EM PONTOS FICOU: {Nota}")
else : print("REPROVADO")