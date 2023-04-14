 def gera():
    var = 'Valor 1'
    yield var
    var = 'Valor 2'
    yield var
    var = 'Valor 3'
    yield var
g=gera()

for v in g:
    print(v)

lista = list(range(10))
lista2 = [x for x in range(10)]
print(f'{lista} \n {lista2}')