meses = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}

numero_mes = int(input())


if 1 <= numero_mes <= 12:
    nome_mes = meses[numero_mes]
    print(nome_mes)
else:
    print("Número de mês inválido. Por favor, insira um valor entre 1 e 12.")
