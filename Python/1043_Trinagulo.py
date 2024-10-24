A, B, C = map(float, input().split())

# A soma de dois lados deve ser sempre menor que o terceiro lado 
# A medida de qualquer um dos lados deve ser menor que a soma das medidas dos outros dois 
# A medida de qualquer um dos lados deve ser maior que a diferença entre as medidas dos outros dois 
# 3 condições para verificar se forma um triangulo

if A < B + C and B < A + C and C < A + B: 
    print(f"Perimetro = {A + B + C:.1f}")

else:
    print(f"Area = {C * (A + B) / 2 :.1f}")

