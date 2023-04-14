#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 10:31:18 2022

@author: julioferrer
"""
# gera uma lista, e multiplica toda a lista por 2
l1 = [1,2,3,4,5,6,7,8,9]
l2 = [variavel*2  for variavel in l1]
# gera o valor 0,1 e 2 para cada valor dentro da lista 
l3 = [(v,v2) for v in l1 for v2 in range(3)]
# l3 = valor 1 e valor 2 para cada valor na lista l1, para v2, utilize o range 3
# gera uma lista com os parametros v e v2 
# o parâmetro v recebe l1 e v2 recebe range 3


# lista com 3 nomes
l4= ['luiz','mauro','maria']
# recoloque cada valor de a para '@' e coloque tudo em maiúsculo
ex4 = [v.replace('a','@').upper() for v in l4]
# o for recebe cada valor dentro da lista. o for entra como list comprehension

#gera uma tupla
tupla=(
       ('chave','valor'),
       ('chave','valor'),)
# inverte a chave e o valor
ex5 = [(y,x) for x,y in tupla]
# y e x para x e y na tupla



# gera uma lista de 0 a 99
l5 = list(range(100))
# ex6 = v é cada valor de l5 se for divisível por 2 e por 8
ex6 = [v for v in l5 if v % 2 == 0 if v % 8 ==0 ]
# ex7 = valor para cada valor divisível por 3 em l5 se não, o valor vira:'_'
ex7= [v if v % 3 ==0 else '_' for v in l5]

