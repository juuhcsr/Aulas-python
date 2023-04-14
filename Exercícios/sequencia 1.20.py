totalseq=0
acumulado =0
total = list(range(1,21,1))
for n in total:
    totalseq=   f'1/{n}'
    print (totalseq)
    totalseq = 1/n
    acumulado += totalseq
print(f'{acumulado:.2f}')