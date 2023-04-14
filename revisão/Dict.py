# transforma uma lista em um dict e executa funções nos dois valores
'''
lista = [('chave','Valor'),('chave2','Valor2'),]
d1 = {x.upper(): y*2 for x,y in lista} #x e y recebem chave,valor da lista, o x fica maiúsculo e o y é multiplicado e viram um dict
print(d1)
'''
# cria um dict com valores x para chave e multiplica o valor de cada chave por 2
'''
d2 = {f'chave{x}':x**2 for x in range(5)}
print(d2,type(d2))
'''