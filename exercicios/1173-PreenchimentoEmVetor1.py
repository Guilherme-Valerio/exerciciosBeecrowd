V = int(input())

N = [0] * 10
N[0] = V

print(f'N[0] = {N[0]}')

for i in range(1, 10):
    N[i] = N[i-1] * 2
    print(f'N[{i}] = {N[i]}')