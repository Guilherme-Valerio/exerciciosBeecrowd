N = [0] * 20
cont = 0

while cont < 20:
    valor = int(input())
    N[19 - cont] = valor
    cont += 1

cont1 = 0
while cont1 < 20:
    print(f'N[{cont1}] = {N[cont1]}')
    cont1 += 1