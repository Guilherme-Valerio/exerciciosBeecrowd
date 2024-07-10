N = int(input())

if N > 5 and N < 2000:
    for i in range(1, N + 1):
        if i % 2 == 0:
            NN = i ** 2
            print(f'{i}^2 = {NN}')
else:
    print('Valor Inválido')