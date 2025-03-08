import pandas as pd
#region (DICAS)
'''
Sempre faça a comparação por tabela para filtar o que deseja.

print(Planilha[Planilha['Valor']>500]) - retorno somenta os valores maiores que 500
print(Planilha['Valor'>500]) - retorna se e true ou false

'''
#endregion

Planilha = pd.read_excel(r"C:\Users\marmi\OneDrive\Documentos\GitHub\Ed-Estudos\Python\Python_Excel\Pandas\ESTUDO.xlsx")
print(Planilha)

# como criar um nova coluna
Planilha['Metadinha'] = Planilha['Valor']/2

#como criar um filtro duplo
Marcador_ac_500 = Planilha['Valor']>500
Marcador_ac_600 = Planilha['Valor']<600
print(Planilha[Marcador_ac_500&Marcador_ac_600])

Planilha.info()
#como salvar em outro arquivo
Planilha.to_excel(r"C:\Users\marmi\OneDrive\Documentos\GitHub\Ed-Estudos\Python\Python_Excel\Pandas\RESULTADO.xlsx", index=False)