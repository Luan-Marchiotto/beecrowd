x, y = map(float, input().split())

# Verifica se o ponto está na origem
if x == 0 and y == 0:
    print("Origem")

# Verifica se o ponto está sobre o eixo Y
elif x == 0:
    print("Eixo Y")

# Verifica se o ponto está sobre o eixo X
elif y == 0:
    print("Eixo X")

# Verifica os quadrantes
elif x > 0 and y > 0:
    print("Q1")

elif x < 0 and y > 0:
    print("Q2")

elif x < 0 and y < 0:
    print("Q3")

else:
    print("Q4")
