a, b, c = map(int, input().split())

# valores em uma lista
valores = [a, b, c]

# cópia da lista e ordene-a
ordenados = sorted(valores)

# valores ordenados
for valor in ordenados:
    print(valor)

print()

# ordem original
for valor in valores:
    print(valor)