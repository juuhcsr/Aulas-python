
# como fazer lista de range e enumerar o indicie
#como desempacotar uma lista
# como acessar índice da lista
# funções split, strip, upper e count
# outro exemplo de split + enumerate - indicando índice
#como definir range de listas

'''

# como fazer lista de range
#como enumerar um índice

l3 = list(range(10,1,-1))
for v1,v2 in enumerate(l3):
    print(v1,v2)

'''
'''
#como desempacotar uma lista
#essa lista desempacota luis e joão

lista =['luis','joão','maria',1,2,3,4,5,6]
na1, na2, *resto = lista
print(na1,na2)
print(resto)
'''
'''

# como acessar índice do dicionário 

horas=['Bom dia','Boa Tarde','Boa Noite']
print(horas[0])


'''

# funções split, strip, upper e count

'''

frase = 'O Brasil é o país do futebol, o Brasil é penta.'
lista = frase.split(' ') #divide a frase por , a cada espaço e joga em uma lista cada palavra
lista_1 = frase.split(',') # divide a frase por por , a cada vírgula na frase
palavra =''
cont = 0
for valor in lista:
    print(valor.strip().upper()) #strip- remove espaço do ínicio e do final # upper- transforma em maiúscula
    qtd_vezes = lista.count(valor) # conta quantas vezes tem esse valor na lista
    if qtd_vezes > cont: 
        cont = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes é {palavra} ({cont} x)')  
'''

# outro exemplo de split + enumerate - indicando índice

'''
#lista =['O','Brasil','é','Penta']
st = 'O Brasil é penta. '
lista = st.split(' ')
for v1, v2 in enumerate(lista):
    print(v1, v2)

#como definir range de listas

lista = list(range(10))
lista2 = [x for x in range(10)]
print(f'{lista} \n {lista2}')
'''

# gera uma lista, e multiplica toda a lista por 2 e range dentro de lista com for

'''
l1 = [1,2,3,4,5,6,7,8,9]
l2 = [variavel*2  for variavel in l1]
# gera o valor 0,1 e 2 para cada valor dentro da lista
l3 = [(v,v2) for v in l1 for v2 in range(3)]
# o parâmetro v recebe l1 e v2 recebe range 3
'''
# indicando índice com count
'''
from itertools import count
contador = count()
lista = ['joão','maria','joana','estelar']
lista = zip (contador,lista)
print(list(lista))
'''

# recoloca cada valor de a para '@' e coloque tudo em maiúsculo

'''
l4= ['luiz','mauro','maria']
ex4 = [v.replace('a','@').upper() for v in l4]
'''
# inverte a chave e o valor de uma tupla
#     ex5 = [(y,x) for x,y in tupla]


# if e else com for dentro de listas
'''
l5 = list(range(100))
ex6 = [v for v in l5 if v % 2 == 0 if v % 8 ==0 ] # v é cada valor divisível por 2 e por 8
ex7= [v if v % 3 ==0 else '_' for v in l5]# v é cada valor divisível por 3 se não for, vira _
'''
# divide a frase a cada n de 'letras'
'''
n=3
lista = [string[i:i + n] for i in range(0, len(string),n)]
print(lista)
# coloca um . na divisão das listas
retorno = '.'.join(lista)
'''

# organiza lista pelo segundo indicie do maior pro menor sem alterar a lista


'''
lista = [ ['p1',13],['p2',6],['p3',8],['p4',10],['p5',50],]

print(sorted(lista,key=lambda item:item[1],reverse=True))
print(lista)
'''
