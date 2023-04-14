string = '0123456789012345678901234567890123456789012345678901234567890123456789'
n = 10
# lista = range de 10 a 10 para cada numero no range de 0 até len da string
lista = [string[i:i + n] for i in range(0, len(string), n)]
print(lista)
retorno = '.'.join(lista)
print(retorno)

