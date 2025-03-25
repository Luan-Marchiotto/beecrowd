repeticao = int(input())  # Número de produtos comprados
soma = 0

precos = {
    1001: 1.50,
    1002: 2.50,
    1003: 3.50,
    1004: 4.50,
    1005: 5.50
}

for _ in range(repeticao):
    produto, quantidade = map(int, input().split())
    
    if produto in precos:
        soma += precos[produto] * quantidade

print(f"{soma:.2f}")