M = [[] for _ in range(12)]
O = input()

for i in range(12):
    for k in range(12):
        x = float(input())
        M[i].append(x)
        
soma = []

for i in range(11):
    for j in range(i + 1, 12):
        soma.append(M[i][j])

if O == 'S':
    somafim = sum(soma)
    print(f'{somafim:.1f}')
elif O == 'M':
    media = sum(soma) / len(soma)
    print(f'{media:.1f}')
else:
    print("Operação inválida. Digite 'S' ou 'M'.")