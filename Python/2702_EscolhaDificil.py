frango, bife, massa = map(int, input().split())  # Pratos disponíveis

frango_pedido, bife_pedido, massa_pedido = map(int, input().split())  # Pedidos feitos

soma = 0

if frango < frango_pedido:
    soma += frango_pedido - frango

if bife < bife_pedido:
    soma += bife_pedido - bife

if massa < massa_pedido:
    soma += massa_pedido - massa

print(soma)