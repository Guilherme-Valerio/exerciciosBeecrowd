x = [0] * 10
i = 0

while True:
    try:
        if i <= 10:
            num = int(input())
            x[i] = num
            if num <= 0:
                x[i] = 1
            print(f"X[{i}] = {x[i]}")
            i += 1    
    except EOFError:
        break