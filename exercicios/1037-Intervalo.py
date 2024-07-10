n1 = float(input())

if n1 >= 0 and n1 <= 25:
    print(f'Intervalo [0,25]')
elif n1 > 25 and n1 <= 50:
    print(f'Intervalo (25,50]')
elif n1 > 50 and n1 <= 75:
    print(f'Intervalo (50,75]')
elif n1 > 75 and n1 <= 100:
    print(f'Intervalo (75,100]')
else:
    print(f'Fora de intervalo')
    
    