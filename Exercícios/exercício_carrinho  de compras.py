
#cria um dict vazio
carrinho = []
# adiciona valores pra lista
carrinho.append(('produto 1',30))
carrinho.append(('produto 2',20))
carrinho.append(('produto 3',50))
print(carrinho)
total = sum([float(y) for x,y in carrinho])
print(total)
