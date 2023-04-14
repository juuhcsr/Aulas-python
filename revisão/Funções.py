
# quantas letras tem na string
'''
frase = 'O rato roeu a roupa do rei de roma'
tamanho_frase =len(frase) # quantas letras tem na string
cont = 0
nstring = ''
letra_maiuscula = input("qual letra você quer que seja maiuscula ?: ")
while cont < tamanho_frase:
    letra = frase[cont] # o valor de letra é o valor de frase dentro do contador, ou seja pra cada vez que o contador rodar, vai mudar o valor da letra
    if letra == letra_maiuscula:
        nstring += letra_maiuscula.upper() #gera uma nova string, se a letra foi igual a escolhida, ela sera maiúscula
    else:
        nstring += letra # adiciona o valor de nstring + o valor da letra
    cont += 1 # adiciona valor pro contador
    print(nstring)
'''

