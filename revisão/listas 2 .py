# como copiar uma lista sem indicar o mesmo objeto

'''

#método 1

numeros = [1,2,3,4,5]
novos_numeros=numeros.copy()
novos_numeros[0] = 20
print(numeros)

método 2

numeros = [1,2,3,4,5]
novos_numeros = [numero for numero in numeros]
print (novos_numeros)

método 3

numeros = [1,2,3,4,5]
novos_numeros=[]
for numero in numeros:
    novos_numeros.append(numero)
print(novos_numeros)

'''

# calculadora com função

'''

def divisaofn(x,y):
    return x/y
def multfn(x,y):
    return x*y
def potfn(x,y):
    return x**y

#Método 1 - com listas + for, porém para lista
numeros = [1,2,3,4,5]
divisao = [numero/2 for numero in numeros]
mult = [numero*2 for numero in numeros]
quadrado = [numero**2 for numero in numeros]

#Método 2 - usando função no for
divisao = [divisaofn(numero, 2) for numero in numeros]
mult = [multfn(numero, 2) for numero in numeros]
quadrado = [potfn(numero, 2) for numero in numeros]
print(numeros)
print(divisao)
print(mult)
print(quadrado)
'''

# estruras condicionais if e for dentro da lista

'''
numeros = [1,2,3,4,5,6,7,8,9,10]
novos_numeros=[num for num in numeros if num > 5]  #para maiores que 5
pares=[num for num in numeros if num %2 == 0] # para pares
impares=[num for num in numeros if num %2 == 0] # para impares
nova_lista=[
    num if num != 6 # se o numero for diferente de 6, continua o for
    else 600  # se não, ou seja, se for 6, o numero é 600
    for num in pares
    ]
print(nova_lista)
'''

# linhas e colunas

'''
linhas_e_colunas = [(x,y) # dois valores # lista 1,1 1,2 .. 2,1 2,2 ...
    #if y !=2 else (x,y *5) # se y for diferente de 2 continua se não, multiplica por 5
    for x in range(1,5) 
    for y in range(1,5)
        ]
print(linhas_e_colunas)

'''

#strings
# coloca a ultima letra de cada nome em maiúsculo
# divide o nome e coloca . a cada 2 letras
'''
string ='Otávio Miranda'
numero_de_letras = 2
nova_string = '.'.join([
    string[indice:indice+numero_de_letras] 
    for indice in range(0,len(string),numero_de_letras)])
print(nova_string)

# coloca a ultima letra de cada nome em maiúsculo

nomes = ['luiz','maria','maria','helena','Joana','felipe']
novos_nomes = [f'{nome[:-1].lower()}{nome[-1].upper()}'for nome in nomes]    #.title - 1 maiuscula
print(novos_nomes)
'''




#flat
# para cada x em numeros eu tenho uma lista
'''
numeros = [[numero,numero**2]for numero in range(10)]
flat = [y for x in numeros for y in x] # para cada x em numeros eu tenho uma lista
print(flat)
'''

#lambda


'''
def funcao(arg,agr2):
    return arg * agr2

var = funcao(2,2)
a = lambda x,y: x*y
print(var, a)
'''
#organizando uma lista em ordem do menor pro maior 
'''
lista =[ ['p1',7], ['p2',33], ['p3',67], ['p4',50], ['p5',32],  ['p6',24],]
lista.sort(key=lambda item:item[1], reverse = True)
print(lista)
print(sorted(lista,key=lambda i:i[1], reverse=True # outro jeito sem lambda
'''
