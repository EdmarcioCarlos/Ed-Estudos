#region (Atividade- 4)
"""
Criar programa para validar login
1 - Usurario deve digitar o seu:
Username
Senha

No sistema crie um usuario e senha de acordo
Username: admin
Senha: 123456

sistema deve mostrar
Certo: Login ok
Errado: Usurario e senha incorretos.
"""
#endregion

Usuario_Banco = 'admin'
Senha_Banco = 123456

Tentativa_User = input('Digite o usuario: ')
Tentativa_Senha = int(input('Digite a senha:'))

if Tentativa_User == Usuario_Banco and Tentativa_Senha == Senha_Banco:
    print(f'!Login correto! Seja bem vindo {Usuario_Banco}')
else:
    print('! Usuario ou senha incorreto!')
