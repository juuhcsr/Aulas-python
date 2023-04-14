horas=['Bom dia','Boa Tarde','Boa Noite']
i = int(input("Digite que horas são: "))
if i < 11:
    print(horas[0])
if i > 11 and i < 17:
    print(horas[1])
if i > 17 and i < 23:
    print(horas[2])