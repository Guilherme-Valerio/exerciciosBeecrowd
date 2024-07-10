M = [[] for _ in range(12)]
O = input()

for i in range(12):
    for j in range(12):
        x = float(input())
        M[i].append(x)

soma = []
cont = 0
col = 11

for i in range(1,11):
    for j in range(col,12):
        soma.append(M[i][j])
        
        cont += 1
    if i < 5:
        col -= 1
    if i > 5:
        col += 1

if O == 'S':
    print(f"{sum(soma):.1f}")
elif O == 'M':
    print(f"{sum(soma) / len(soma):.1f}")
else:
    print("Operação inválida. Digite 'S' ou 'M'.")