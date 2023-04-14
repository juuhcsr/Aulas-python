# calculadora com função
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

print(f'{numeros}\n{divisao}\n{mult}\n{quadrado}')