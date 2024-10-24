from math import sqrt
A, B, C = map(float, input().split())

delta = pow(B,2) - 4 * A * C

if delta < 0 or A == 0:
    print("Impossivel calcular")
else: 
    raiz1 = (-B + sqrt(delta)) / (2 * A)
    raiz2 = (-B - sqrt(delta)) / (2 * A)
    print(f'R1 = {raiz1:.5f}')
    print(f'R2 = {raiz2:.5f}')