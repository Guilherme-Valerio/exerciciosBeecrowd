N = []
while True:
    x = int(input())
    if x < 0:
        break
    N.append(x)
media = sum(N) / len(N)
print(f'{media:.2f}')