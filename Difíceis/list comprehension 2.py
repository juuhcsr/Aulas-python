'''
numeros = [1,2,3,4,5]
novos_numeros=numeros.copy() #utilizando o copy, copiamos a lista e n nos referenciamos mais a ela
novos_numeros[0] = 20
print(numeros)

# as duas var apontas o mesmo valor na memória então uma altera a outra

numeros = [1,2,3,4,5]
novos_numeros = [numero for numero in numeros]
print (novos_numeros)


numeros = [1,2,3,4,5]
novos_numeros=[]
for numero in numeros:
    novos_numeros.append(numero)
print(novos_numeros)
# é a mesma coisa só que muito maior 


def divisaofn(x,y):
    return x/y
def multfn(x,y):
    return x*y
def potfn(x,y):
    return x**y

numeros = [1,2,3,4,5]

divisao = [numero/2 for numero in numeros]
mult = [numero*2 for numero in numeros]
quadrado = [numero**2 for numero in numeros]
# para cada numero na lista vai ser multiplicado por dois 

divisao = [divisaofn(numero, 2) for numero in numeros]
mult = [multfn(numero, 2) for numero in numeros]
quadrado = [potfn(numero, 2) for numero in numeros]


print(numeros)
print(divisao)
print(mult)
print(quadrado)


# estruras condicionais
numeros = [1,2,3,4,5,6,7,8,9,10]
novos_numeros=[num for num in numeros if num > 5]  #para maiores que 5
pares=[num for num in numeros if num %2 == 0] # para pares
impares=[num for num in numeros if num %2 == 0] # para impares
outro_if=[
    num 
    if num != 6 # se o numero for diferente de 6, continua o for
    else 600  # se não, ou seja, se for 6, o numero é 600
    for num in pares
    ]
print(outro_if)

# linhas e colunas

linhas_e_colunas = [
    (x,y)
    if y !=2 else (x,y *1000)   
    for x in range(1,11)
    for y in range(1,6)
    if x !=2
        ]
print(linhas_e_colunas)


#strings

string ='Otávio Miranda'
numero_de_letras = 2
nova_string = '.'.join([
    string[indice:indice+numero_de_letras]
    for indice in range(0,len(string),numero_de_letras)])
print(nova_string)


nomes = ['luiz','maria','maria','helena','Joana','felipe']
novos_nomes = [f'{nome[:-1].lower()}{nome[-1].upper()}'for nome in nomes]    #.title - 1 maiuscula
print(novos_nomes)
'''
#flat
numeros = [[numero,numero**2]for numero in range(10)]
flat = [y for x in numeros for y in x] # para cada x em numeros eu tenho uma lista
print(flat)





