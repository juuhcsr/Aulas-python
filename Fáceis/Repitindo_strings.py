frase = 'O rato roeu a roupa do rei de roma'
t=len(frase)
cont = 0
nstring = ''
le = input("qual letra você quer que seja maiuscula ?: ")
while cont < t:
    letra = frase[cont]
    if letra == le:
        nstring += le.upper()
    else:
        nstring += letra
    cont += 1
    print(nstring)