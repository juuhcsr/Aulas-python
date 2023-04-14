#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 11:46:51 2022

@author: julioferrer

# crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da
# função 2
def ola_mundo():
    return 'Olá mundo!'

def mestre(funcao):
    return funcao()

execu = mestre(ola_mundo)
print(execu)



#crie uma função que recebe uma função 2 como parametro e retorne o valor da func2
# executada. faça a função 1 exercutar duas funções que recebam um número diferente de 
#argumentos 


def mensagem():
    return 'ola mundo'
    
def mensagem_com():
    return 'seja bem vinda a terra'
    
def mestre(fun,cao):
    return fun(),cao()

x = mestre(mensagem,mensagem_com)
print (x)
"""
def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def fala_oi(nome):
    return f'Oi {nome}'


def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'


executando = mestre(fala_oi, 'Luiz')
executando2 = mestre(saudacao, 'Luiz', 'Bom dia!')
print(executando)
print(executando2)