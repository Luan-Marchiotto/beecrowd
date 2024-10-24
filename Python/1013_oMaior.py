a, b, c = map(int, input().split())

maior = (int(a) + int(b) + abs(int(a) - int(b)))  / 2
resultado = (int(maior) + int(c) + abs(int(maior) - int(c)))/2

print(f"{resultado:.0f} eh o maior")