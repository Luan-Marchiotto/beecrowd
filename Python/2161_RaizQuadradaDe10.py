def raiz(rep):
    if rep == 0:
        return 6
    
    resultado = 6 + (1 / raiz(rep-1))
    return resultado

rep = int(input())

resultado = raiz(rep)-3

print(f'{resultado:.10f}')