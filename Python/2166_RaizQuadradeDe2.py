def raiz(rep):
    if rep == 0:
        return 2
    
    resultado = 2 + (1 / raiz(rep-1))
    return resultado

rep = int(input())

resultado = raiz(rep) - 1

print(f'{resultado:.10f}')