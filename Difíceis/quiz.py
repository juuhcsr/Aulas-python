#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 15:20:09 2022

@author: julioferrer
"""
print("texto explicativo :D")
resposta1=0
perguntas = {               #dict perguntas
    'pergunta1': {           # dict cada pergunta tem um dict dentro do dict perguntas
        'pergunta': 'quanto é 2+2',
        'respostas': {'a':'1','b':'4','c':'5',},    # as respostas também possuem um dict
        'resposta_certa':'b',         # cada dict pergunta tem 3 sub-dicts pergunta, resposta e resposta certa
        },
    'pergunta2': {
        'pergunta': 'quanto é 3*2',
        'respostas': {'a':'4','b':'10','c':'6',},
        'resposta_certa':'c',
        },
     'pergunta3': {
        'pergunta': 'quanto é 1*2',
        'respostas': {'a':'4','b':'2','c':'6',},
        'resposta_certa':'b',
        },
     'pergunta4': {
        'pergunta': 'qual a diferença de 6 e 4 ',
        'respostas': {'a':'4','b':'2','c':'6',},
        'resposta_certa':'b',
        },
     'pergunta5': {
        'pergunta': 'quanto é 2 + 2 ? ',
        'respostas': {'a':'peixe','b':'22','c':'4',},
        'resposta_certa':'c',
        },
    
}
print()


for pk, pv in perguntas.items():  # pk é a pergunta, esse for acessa as 5 perguntas
    print(f'{pk}: {pv["pergunta"]}') # pv é a primeira pergunta, nele eu acessei
    print("Respostas: ")   # pv seria o dict pergunta mas como eu coloquei {pv["pergunta"]}
                                # eu acessei o dict pv e o subdict pergunta
    for rk, rv in pv['respostas'].items(): # esse for puxa o que ta dentro das respostas
        print(f'[{rk}]: {rv}')    # ele entrega o numero da resposta e o valor da resposta
        # esse for vai repetir as respostas e o de cima vai repetir as perguntas
        
    resposta=input("Qual sua resposta ?: ")  # perguntando qual é a resposta
    
    if resposta == pv['resposta_certa']:     # compara o subdict pergunta['resposta certa']
        print("\n você acertou") # com a resposta do usuário e se ele acertar, soma um a var
        resposta1 += 1
    else:
        print('\nvocê errou')
    print()
qnt_perguntas = len(perguntas)
porcentagem_acerto = resposta1 /qnt_perguntas*100

print(f' você acertou {resposta1} respostas.')
print(f'sua porcentagem de acerto foi de {porcentagem_acerto}%')