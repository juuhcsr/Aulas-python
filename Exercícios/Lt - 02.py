#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 11:18:59 2022

@author: julioferrer
"""

# exercício 1 

x = int(input("defina um valor pra x: "))
if (x % 2 == 0):
    print("ele é par")
else:
    print("ele é impar")
    
    
# exercício 2 

x=int (input('digite o valor de x: '))
y=int (input('digite o valor de y: '))
z=int (input('digite o valor de z: '))
lista = [x,y,z]
if x == y or x == z or y == z :
    print("numeros iguais na sequência")
lista.sort()
print(lista)
                

# exercício 3 
# ler o nome do func e o total de comissÃ£o que vai receber 
def gh(n):
    n = (x * 1.5)
    return n

def fh(n):  
    n = (x * 2)
    return n

nome = (input("qual o nome do funcionÃ¡rio: "))  
x = float(input("quantos produtos foram vendidos: "))
y = x
if x >= 250 and x < 500:
    y = gh(x)
    
elif x > 500:
    y = fh(x)
    
print (f"o funcionÃ¡rio {nome} fez {x} vendas e obteve {y} reais")
    
#exercício 4 

def soma(x,y):
    z = x + y 
    return z 
def sub(x,y):
    z = x - y 
    return z 
def mult(x,y):
    z = x*y 
    return z 
def div(x,y):
    z = x/y 
    return z 
z=0
x = int(input("digite o valor de x: "))
y = int(input("digite o valor de y: "))

g = input('''digite a operação desejada: 
          + - para soma
          - - para subtração0
          * - para multiplicação
          / - para divisão 
          digite a operação desejada: ''')
if g =='+':
    z=soma(x,y)
elif g == '-':
    z=sub(x,y)
elif g == '*':
    z=mult(x,y)
elif g == '/':
    z=div(x,y)
else:
    print("operador inválido")
print (f" o valor de {x}{g}{y} é {z}")

#exercício 5 

candidatos = {1:'João Ninguém',2:'Maria da silva',3:'José da esquina',4:'Manuel portuga',5:'Branco'}
for num, cand in candidatos.items():
    print(f"numero: {num} candidato {cand}")
ca = int(input ("Para qual candidato você quer votar ?: "))
if ca >= 1 and ca <= 4:
    print(f'você votou no candidato {candidatos[ca]}')
elif ca == 5:
    print('você votou em branco')
else:
    print("voto nulo")  


