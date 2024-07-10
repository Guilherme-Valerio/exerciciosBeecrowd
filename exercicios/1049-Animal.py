palavra1 = input()
palavra2 = input()
palavra3 = input()

if palavra1 == 'vertebrado':
    if palavra2 == 'ave':
        if palavra3 == 'carnivoro':
            print(f'aguia')
        else:
            print(f'pomba')
    else:
        if palavra3 == 'onivoro':
            print(f'homem')
        else:
            print(f'vaca')
else:
    if palavra2 == 'inseto':
        if palavra3 == 'hematofago':
            print(f'pulga')
        else:
            print(f'lagarta')
    else:
        if palavra3 == 'hematofago':
            print(f'sanguessuga')
        else:
            print(f'minhoca')