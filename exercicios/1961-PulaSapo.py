P, N = [int(x) for x in input().strip().split()]
H = list(map(int, input().split()))

for i in range(N - 1):
    dif = abs(H[i] - H[i+1])
    if dif > P:
        print('GAME OVER')
        exit()
print('YOU WIN')