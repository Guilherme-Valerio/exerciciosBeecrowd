nota = [float(x) for x in input().strip().split(' ')]

media = ((nota[0] * 2) + (nota[1] * 3) + (nota[2] * 4) + (nota[3] * 1)) / (2 + 3 + 4 + 1)

print(f'Media: {media:.1f}')

if media >= 7.0:
    print('Aluno aprovado.')
elif media < 5.0:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    
    notaexame = float(input().strip())
    
    print(f'Nota do exame: {notaexame:.1f}')
    
    media = (notaexame + media) / 2
    if media >= 5.0:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
        
    print(f'Media final: {media:.1f}')