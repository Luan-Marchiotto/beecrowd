rep = int(input())

for _ in range(rep):
    ano = int(input())
    
    resultado = ano - 2015
    
    if resultado > 0:
        print(f"{resultado + 1} A.C.")
    elif resultado < 0:
        print(f"{abs(resultado)} D.C.")
    else:
        print("1 A.C.")