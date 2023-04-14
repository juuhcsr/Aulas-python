string = 'O Brasil é o país do futebol, o Brasil é penta.'
lista = string.split(' ')
lista_1 = string.split(',')
palavra =''
cont = 0

for valor in lista:
    print(valor.strip().upper())




""" 
   qtd_vezes = lista.count(valor)
    if qtd_vezes > cont:
        cont = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes é {palavra} ({cont} x)')
"""