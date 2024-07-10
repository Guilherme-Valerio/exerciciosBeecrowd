while True:
    try:
        
        cursos = {'EPR': 0, 'EHD': 0, 'INTRUSOS': 0} 
        voltas = int(input())
        for i in range(voltas):
            aluno = input().split()
            if aluno[1] == "EPR":
                cursos['EPR'] += 1
            elif aluno[1] == "EHD":
                cursos['EHD']+= 1
            else:
                cursos['INTRUSOS']+= 1
            
        print(f"EPR: {cursos['EPR']}")
        print(f"EHD: {cursos['EHD']}")
        print(f"INTRUSOS: {cursos['INTRUSOS']}")
        
    except EOFError:
        break