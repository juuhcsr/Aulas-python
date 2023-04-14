# crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função 2

'''
def funcao2():
    return 2*7
# definindo função que retorna a string olá mundo
def ola_mundo():
    return 'Olá mundo!'
# definindo função que retorna uma função
def mestre(funcao):
    return funcao()
# aqui você imprimi a função mestre que pode retornar várias funções
print(mestre(ola_mundo))
print(mestre(funcao2))
'''

'''
crie uma função que recebe uma função 2 como parametro e retorne o valor da func2
executada. faça a função 1 exercutar duas funções que recebam um número diferente de 
argumentos
'''
# crie uma função que retorne duas funções
'''
def mensagem():
    return 'ola mundo'


def mensagem_com():
    return 'seja bem vinda a terra'


def mestre(funcao1, funcao2):
    return funcao1(), funcao2()


x = mestre(mensagem, mensagem_com)
print(x)
'''
# args e kwargs com funções
# define função que recebe n argumentos
def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)
# retorna os valores

def fala_oi(nome):
    return f'Oi {nome}'

# função para retornar oi e o variável dentro da atribuição

def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'


executando = mestre(fala_oi, 'Luiz')
executando2 = mestre(saudacao, 'Luiz', 'Bom dia!')
print(executando)
print(executando2)
