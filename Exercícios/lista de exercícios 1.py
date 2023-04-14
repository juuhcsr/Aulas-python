'''
1) Leia o nome do aluno, o nome da disciplina, o número da turma e as três notas de um aluno e imprima os
dados lidos e a média aritmética das notas (soma das notas divido por três).

# Le o nome do aluno, nome da disciplica e o numera da turma
nome = input("digite o nome do aluno: ")
disciplina = input("digite o nome da disciplica: ")
turma = input("digite o nome da turma: ")

# le as 3 notas
nota1= int(input("digite a primeira nota: "))
nota2= int(input("digite a segunda nota: "))
nota3= int(input("digite a terceira nota: "))

# soma as notas

notafinal = float(nota1+nota2+nota3)/3
notafinal=round(notafinal,2)
print(f"o aluno {nome} da turma {turma} teve a média das notas de {notafinal:.2f} na matéria {disciplina}")


2) Em uma loja, existe um total mensal de vendas. Faça a leitura de todos os totais de um ano juntamente com
o nome da loja. Depois, imprima o nome da loja e os totais de vendas semestrais.

total =0
meses = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
for i in meses:
    mes = float(input(f'digite o valor dos ganhos de {i}: '))
    total += mes
    print (f' os ganhos de {i} foram de {mes} o total acumulado é de {total}')
print(f'o total ganho nos doze meses é de `{total}')

3) Leia os seguintes dados de uma conta corrente: o nome do correntista, o nome do banco, o número da conta,
o valor total de cheques a debitar, o total de dinheiro e cheques a creditar, o limite de crédito e o saldo atual.
Retorne impresso o nome do correntista, o nome do banco, o número da conta e o saldo disponível (Saldo
disponível = (saldo atual + valor de crédito + limite) - valor de débito).

'''
#contas =['nome_correntista','nome_do_banco','numero_da_conta','total_a_debitar','total_em_dinheiro','cheques a creditar','limite_de_crédito','saldo_atual']
contas =['nome_correntista','nome_do_banco']
count = list(range(1,3) )
contas = [v.replace('_',' ') for v in contas]
cont = 's'
conta1=[]
while cont == 's':
    for n in contas:
        m = input(f'digite o valor de {n}: ')
        conta1.append(m)
    cont=input('quer continuar?')
print(conta1:-1)






'''

3) Leia os seguintes dados de uma conta corrente: o nome do correntista, o nome do banco, o número da conta,
o valor total de cheques a debitar, o total de dinheiro e cheques a creditar, o limite de crédito e o saldo atual.
Retorne impresso o nome do correntista, o nome do banco, o número da conta e o saldo disponível (Saldo
disponível = (saldo atual + valor de crédito + limite) - valor de débito).
4) Faça um algoritmo que leia o valor de troca de um dólar por um real e o valor de uma quantia em dólar.
Após imprima quantos reais dão a quantia de dólares lida.
5) O preço de um produto ao consumidor é a soma do preço de custo mais a porcentagem dos impostos e a

porcentagem do distribuidor. Faça um algoritmo que leia o nome do produto, o seu custo de fábrica e as ta-
xas de impostoe de distribuição. Imprima o nome e o preço final ao consumidor deste produto.
'''