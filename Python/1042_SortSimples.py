a, b, c = map(int, input().split())

valores = [a, b, c]

ordenados = sorted(valores)

# valores ordenados
for valor in ordenados:
    print(valor)

print()

# ordem original
for valor in valores:
    print(valor)