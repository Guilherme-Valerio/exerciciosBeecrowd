X = int(input())
Y = int(input())

soma_impares = 0
menor = min(X, Y)
maior = max(X, Y)

for num in range(menor + 1, maior):
    if num % 2 != 0:  
        soma_impares += num

print(soma_impares)