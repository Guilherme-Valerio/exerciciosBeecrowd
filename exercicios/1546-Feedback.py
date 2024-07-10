voltas = int(input())

nomes = ['Rolien', 'Naej', 'Elehcim', 'Odranoel']

for i in range(voltas):
    k = int(input())
    for j in range(k):
        n1 = int(input())
        print(nomes[n1 - 1])