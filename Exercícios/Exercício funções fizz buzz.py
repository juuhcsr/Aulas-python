
# criar uma função que exibe uma saudação com os parâmetros saudação e nome
'''
def sau(sa1,nome):
    print(sa1,nome)
sab=input("digite sua saudação")
nom=input("digite o nome")
sau(sab,nom)
'''




# criar uma função que recebe 3 numeros e exiba a soma entre eles
'''
def soma(n1,n2,n3):
    return n1+n2+n3
na = int(input("digite o número 1: "))
nb = int(input("digite o número 2: "))
nc = int(input("digite o número 3: "))
soma=soma(na,nb,nc)
print(soma)
'''



'''
crie uma função que receba 2 numeros. o 1 é um valor e o segundo um percentual, retorne
o valor do primeiro somando o percentual do segundo
'''
'''
def per(n1,n2):
    n1 = n1 + (n1 * (n2/100))
    return n1
na = int(input("digite o numero: "))
nb = int(input("digite a porcentagem: "))
v = per(na,nb)
print (v)
print (f"{nb}% de {na} somado a {na} é {v}")
'''



'''
 fizz buss = se o parametro da função for dividido por 3, retorne fizz, se o parâmetro da função
for divisível por 5, retorne buzz. se o parâmetro da função for divisivel por 5 e por 3, retorne fizzbuzz.
caso contrário, retorne o número enviado
'''
'''
def caso3():
    print("Fizz")
def caso5():
    print("Buzz")
def caso3_5():
    print("FizzBuzz")

print('''
|---------------------------------------------------|
|                      FIZZ BUZZ                    |
|---------------------------------------------------|
''')
while True:
    num=int(input("Digite um valor para participar: "))
    if num%3==0 and num%5==0:
        caso3_5()
    elif num % 5 ==0:
        caso5()
    elif num % 3 ==0:
        caso3()
    else:
        print("Não foi hoje que você ganhou")
'''






