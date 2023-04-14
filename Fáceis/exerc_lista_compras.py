# suponha que a gente receba um produto
carrinho = []
0
carrinho.append(('produto 1',30))
carrinho.append(('produto 2',20))
carrinho.append(('produto 3',50))

total = sum([float(y) for x,y in carrinho])
print(total)
#lista = [string[i:i + n] for i in range(0, len(string),n)] 
#ex6 = [v for v in l5 if v % 2 == 0 if v % 8 ==0 ]