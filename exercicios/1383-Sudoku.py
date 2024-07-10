n = int(input())

for i in range(n):
    sudoku = [list(map(int,input().strip().split()))[:9] for _ in range(9)]
    linhas_dif = all(len(set(linha)) == 9 for linha in sudoku)
    colunas_dif = all(len(set(coluna)) == 9 for coluna in zip(*sudoku))
    blocos_dif = all(len(set(sudoku[i][j] for i in range(x, x+3) for j in range(y, y+3))) == 9 
    for x in range(0, 9, 3) for y in range(0, 9, 3))
    
    
    if linhas_dif and colunas_dif and blocos_dif:
        print(f'Instancia {i + 1}')
        print('SIM')
        print('')
    else:
        print(f'Instancia {i + 1}')
        print('NAO')
        print('')