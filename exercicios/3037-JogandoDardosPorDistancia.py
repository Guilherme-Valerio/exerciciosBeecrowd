N = int(input())

for i in range(N):

    pontos_joao = []
    pontos_maria = []

    for j in range(3):
        x, d = map(int, input().split())
        pontos_joao.append(x * d)  
        
    for k in range(3):
        x, d = map(int, input().split())
        pontos_maria.append(x * d)  
        

    if sum(pontos_joao) > sum(pontos_maria):
        print("JOAO")
    else:
        print("MARIA")