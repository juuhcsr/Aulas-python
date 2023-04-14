lista = [
    ['p1',13],
    ['p2',6],
    ['p3',8],
    ['p4',10],
    ['p5',50],
    ]



print(sorted(lista,key=lambda item:item[1],reverse=True))
print(lista)