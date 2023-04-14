#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 12:07:54 2022

@author: julioferrer
"""

lucro10 = 0
lucro15 = 0
lucro20 = 0
porcentagem = 0
cont = 0
acumulado1 = 0
acumulado2 = 0
lucro_total = 0
quantidade = int(input(' Quantos produtos serão consultados?: '))
while quantidade > cont :
    nome = input('digite o nome do produto: ')
    valor_compra = float(input('digite o valor de compra do produto: '))
    valor_venda = float(input('digite o valor de venda do produto: '))
    quant = int(input(' Quantos produtos foram vendidos?: '))
    # lucro = valor de venda - valor de compra
    # em porcentagem pode ser
    # valor de venda - valor de compra
    cont += 1
    porcentagem = (valor_venda/valor_compra*100)-100
    if porcentagem < 10:
        lucro10 += 1
    elif porcentagem >= 10 and porcentagem <= 20:
        lucro15 += 1
    elif porcentagem > 20:
        lucro20 +=1
    acumulado1 += valor_compra*quant
    acumulado2 += valor_venda*quant
        lucro_total += (valor_venda - valor_compra)*quant
print(f'''
      o valor total de compra foi de {acumulado1} 
      o valor total de venda foi de {acumulado2} 
      o valor total de lucro foi de {lucro_total} 
      tiveram produtos com lucro de:
          <10%          ={lucro10}
          >10% e <20%   ={lucro15}
          >20%          ={lucro20}
      ''')