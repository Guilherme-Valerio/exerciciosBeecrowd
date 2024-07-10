N = int(input())

for i in range(N):
    x = int(input())
    count = []
    for j in range(1, x):
        if (x % j == 0):
            count.append(j)
    if sum(count) == x:
        print(f'{x} eh perfeito')
    else:
        print(f'{x} nao eh perfeito')