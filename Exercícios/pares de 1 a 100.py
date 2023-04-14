#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 11:41:08 2022

@author: julioferrer
"""
# isso é um jeito de pegar a lista de 0 a 100 só os pares
lista = list(range(0,101,2))
print(lista)
 
# esse é outro jeito
lista = list(range(1,101))
for n in lista:
    if n % 2 == 0 :
        print(f'{n} é par')
    else:
        print(f'{n} é impar')