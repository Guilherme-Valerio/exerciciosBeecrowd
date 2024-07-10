n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())
numeros = [n1, n2, n3, n4, n5]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    
print(f'{len(pares)} valores pares')