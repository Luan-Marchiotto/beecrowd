antigo, novo = map(float,input().split())

resultado = ((novo - antigo) / antigo) * 100

print(f"{resultado:.2f}%")