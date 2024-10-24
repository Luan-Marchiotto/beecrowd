x, y, z = map(float, input().split())

pi = 3.14159

triangulo = (x * z) / 2
circulo = pi * (z * z)
trapezio = z * (x + y) / 2
quadrado = y * y
retangulo = x * y
	
print(f"TRIANGULO: {triangulo:.3f}")
print(f"CIRCULO: {circulo:.3f}")
print(f"TRAPEZIO: {trapezio:.3f}")
print(f"QUADRADO: {quadrado:.3f}")
print(f"RETANGULO: {retangulo:.3f}")