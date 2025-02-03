import math
#region (Calculos basicos)


# Sempre tente fazer calculos matematicos com variaveis do mesmo tipo.
Alunos_presentes = 23
Alunos_ausentes = 17

Quantidade_De_Alunos=Alunos_presentes+Alunos_ausentes;

#print(Quantidade_De_Alunos);

#endregion

#region (Modulos basicos)

#  += Operador de atribuição aumentada

NUm1 = 3.598
#print(NUm1);
#print(round(NUm1,1)); # Round aredonda o valor tanto para cima quanto para baixo o mais proximo caso queira usar a casa decimal deve se colocar a virgula.

NUm2 = 2
#print(pow(NUm2,3)) # Pow realiza a protencia do numero necessia do valor inicial e o valor da potencia

#print(max(1,10,50,70,99)) # max sempre retorno o maior numero de uma lista.

#print(sum([1,3,7])) # sum realiza soma de uma lista;


#endregion

#region (Modulos com a biblioteca math)
#print(math.ceil(4.2)) # Arendonda sempre para cima
#print(math.floor(4.2)) # Arendonda sempre para baixo
#print(math.pow(2,3)) # Realiza potencia de um numero
#endregion

#region (Metodos para STRING)
Mensagem = 'e ae meu povo'
'''
print(Mensagem[2]); # Retorno o caracter baseado no numero dentro do [], [0:10] ou [-100:-1]
print(Mensagem.upper()) # Transforma em letra maiscula
print(Mensagem.lower()) # Transforma em letra minuscula
print(Mensagem.strip()) # Retira os espaços antes do texto
print(Mensagem.replace('povo','povete')) # Altera um texto na variavel para um novo
print(Mensagem.split()) # Separa cada palavra da string
'''

#endregion

#region (Dicas de formatação)
Nome="Edmarcio"
Idade=25

#print(f'O meu nome e {Nome}\nE tenho {Idade} anos de idade') # formatação f-string (Bem melhor pra edição de frases)

# \n - permite fazer quebra de linha em uma variavel.
# \t - permite fazer tabulações igual colunas no excel.
#endregion

#region (Exemplo da tabulação)
Mensagem = 'Nome:\tEdmarcio\nIdade:\t25\nPais:\tBrasil'
#print(Mensagem)
#endregion

#region (Iputs e conversção)
Nome = input('Digite seu nome: ')
Idade = int(input('Digite sua idade: '))
Pais = input('Digite o pais onde mora:')

print(f'Ola meu e {Nome}, tenho {Idade} anos de idade é moro no {Pais}!')

# converção de dado deve ser sempre coloca o tipo de variavel antes do input

#endregion
