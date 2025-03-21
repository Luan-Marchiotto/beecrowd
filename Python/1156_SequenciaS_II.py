S = 1
numerador = 3
denominador = 2

for _ in range(18):
    S += numerador / denominador
    numerador += 2
    denominador *= 2 

print(f"{S:.2f}")