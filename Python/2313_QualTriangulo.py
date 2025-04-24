a,b,c = map(int,input().split())

lados = sorted([a, b, c])
x, y, hip = lados

if x + y > hip:
    if a == b == c:
        print("Valido-Equilatero")
    elif a == b or a == c or b == c:
        print("Valido-Isoceles")
    else:
        print("Valido-Escaleno")
    
    if pow(x,2) + pow(y,2) == pow(hip,2):
        print("Retangulo: S")
    else:
        print("Retangulo: N")
else:
    print("Invalido")