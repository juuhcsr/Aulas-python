'''
logged_user = False
msg = 'usuário logado.' if logged_user else 'usuario precisa logar '
print(msg)
'''
idade = input('qual sua idade?: ')
if not idade.isnumeric():
    print('você precisa digitar apenas números')
else:
    idade=int(idade)
    e_de_maior = (idade >= 18)
    msg = 'pode acessar' if e_de_maior else 'não pode acessar.'
    print(msg)