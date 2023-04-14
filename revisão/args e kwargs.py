'''
#args - usado em função para faze-la receber uma lista de argumentos sem tamanho definido e sem palavra-chave
# args são usados para funções que podem receber vários argumentos sem um valor definido
def funcao(*args):
    for arg in args:
        print(f'argumento de *args: {arg}')
funcao('arg1','arg2','arg3','arg4','arg5')

#kwargs - permite nomear os argumentos e passar para as funções parâmetros com nomes
# permitem nomear funções sem um valor definido
def funcao(**kwargs):
    print(f'**kwargs:{kwargs}')
    for kwarg in kwargs.values():
        print(f'Argumentos de **kwargs: {kwarg}')
funcao(a='kwarg1',b='kwarg2',c='kwarg3')
'''
'''
def func(*args, **kwargs):# define uma função que recebe x args e x kwargs
    print(args) # printa os argumentos da função
    print(kwargs) # printa os kwargs da função
    idade = kwargs.get('idade') # usa o get dos dicts para receber o valor de idade
    if idade is not None:
        print(idade)

lista = [1,2,3,4,5]
lista2 = [6,7,8,9,10]
func(*lista,*lista2, nome ='luiz', sobrenome='antonio', idade = 30)
# nessa função, colocamos os argumentos, depois os kwargs,
'''

# args e kwargs com funções
# define função que recebe n argumentos
'''
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
'''