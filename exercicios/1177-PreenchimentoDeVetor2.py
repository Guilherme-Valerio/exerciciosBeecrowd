N = [0] * 1000
T = int(input())
cont = 0
cont1 = 0

while cont < 1000:
    while cont1 <= T - 1 and cont < 1000:
        N[cont1] = cont1
        print(f'N[{cont}] = {cont1}')
        cont1 += 1
        cont += 1
    cont1 = 0 