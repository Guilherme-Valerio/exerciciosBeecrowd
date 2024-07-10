while True:
    try:
        N = int(input())
        M, L = [int(x) for x in input().strip().split(' ')]
        cartasM = [list(map(int, input().strip().split(' ')))[:N] for _ in range(M)]
        cartasL = [[int(x) for x in input().strip().split(' ')[:N]] for _ in range(L)]
        CM, CL = [int(x) for x in input().strip().split(' ')]
        
        
        if not 1 <= CM <= M or not 1 <= CL <= L:
            print("Valores de CM ou CL estão fora dos limites permitidos.")
            exit()
        
        A = int(input())
        
        if cartasM[CM-1][A-1] > cartasL[CL-1][A-1]:
            print('Marcos')
        elif cartasM[CM-1][A-1] < cartasL[CL-1][A-1]:
            print('Leonardo')
        else:
            print('Empate')
    except EOFError:
        break