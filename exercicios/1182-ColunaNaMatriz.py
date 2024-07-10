M = [[] for _ in range (12)]
C = int(input())
T = input()

for i in range(12):
    linha = [] 
    for j in range(12):
        x = float(input())
        linha.append(x)  
    M[i] = linha
    
coluna_selecionada = [linha[C] for linha in M] 

if T == 'S':
    soma = sum(coluna_selecionada)
    print(f'{soma:.1f}')
elif T == 'M':
    media = sum(coluna_selecionada) / len(coluna_selecionada)
    print(f'{media:.1f}')
else:
    print("Operação inválida. Digite 'S' ou 'M'.")