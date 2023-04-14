from itertools import count
indice = count()
cidades = ['são Paulo','Belo Horizonte','Salvador','Bl0umenal']
Estados = ['SP','MG','BA']

cidades_estados = zip(indice,cidades, Estados)


for indice,estado,cidade in cidades_estados:
    print(indice, estado,cidade)