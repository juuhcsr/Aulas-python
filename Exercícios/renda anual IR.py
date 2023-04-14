# declaração do IR
#Cpf, Nome, Renda anual e número de dependentes

#desconto de 110 por denpendente

#calcular o valor para 500 contribuentes 
#cont = {'cpf':'','nome':'','renda.ano':'','num.dep':''}
x=''
def pri(x,y):
    x = (x * 0.05) - (y * 110)
    return x
def sec(x,y):
    x = (x * 0.1)- (y * 110)
    return x
def ter(x,y):
    x = (x * 0.15)- (y * 110)
    return x

for n in range(2):
    #cpf = input("Digite o Cpf do contribuente: ")
    #nome = input("Digite o nome do contribuente: ")
    renda_ano = int(input("Digite a renda anual do contribuente: "))
    num_dep = int(input("Digite o numero de dependentes do contribuente: "))
    nome ='jc'
    cpf = '335'
    num_dep = 2
    if renda_ano > 900 and renda_ano <= 5000 :
        x = pri(renda_ano,num_dep)
    elif renda_ano > 5000 and renda_ano <= 10000:
        x = sec(renda_ano,num_dep)
    elif renda_ano > 10000:
        x = ter(renda_ano,num_dep)
    if x < 0:
        x = 'nada'
    print(f"o contribuente {nome} do cpf {cpf} tem uma renda anual de {renda_ano} com {num_dep} dependentes e deve {x} para a receita")