# ler o numero do candidato, idade, sexo, experiência em serviço(s/n)
#mostrar a idade média dos candidatos
#mostre o numero total de candidatos
#mostre quais os candidatos maiores de idade que tem experiência no serviço
cont = 0
idade18 = 0
candexp = 0
idademed = 0
quantidade = int(input(' Quantos candidatos serão entrevistados?: '))
while quantidade > cont :
    numero = int(input('digite o numero do candidato: '))
    nome = input('digite o nome do candidato: ')
    idade = int(input('digite a idade do candidato: '))
    if idade > 18:
        idade18 += 1
    idademed += idade
    sexo = input('digite o sexo do candidato: ')
    exp = input('o candidato tem experiência ?: ')
    if exp == 'sim':
        candexp +=1
    cont += 1
idademed = idademed/quantidade
print(f'''
      numero total de candidatos: {quantidade}
      numero maior de idade com experiência: {idade18}
      Média da idade dos candidatos: {idademed}
      
      ''')

