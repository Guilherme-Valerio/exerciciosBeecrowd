M = [[] for _ in range(12)]
L = int(input())
O = input()

for i in range(12):
    for j in range(12):
        x = float(input())
        M[i].append(x)

linha_selecionada = M[L]

if O == 'S':
    soma = sum(linha_selecionada)
    print(f'{soma:.1f}')
elif O == 'M':
    media = sum(linha_selecionada) / len(linha_selecionada)
    print(f'{media:.1f}')
else:
    print("Operação inválida. Digite 'S' ou 'M'.")