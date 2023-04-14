nome=''
while len(nome) <=4 or len(nome) >=6:
    nome = input("Digite seu nome de usuário: ")

    if len(nome) <= 4:
        print("o seu nome é muito pequeno, digite um nome maior")
    elif len(nome) >=6:
        print("o seu nome é muito grande, digite um nome menor")
    else:
        print(f"seu nome é {nome} e atende o requisito de tamanho")