produtos = {
    1: 4.00,
    2: 4.50,
    3: 5.00,
    4: 2.00,
    5: 1.50
} # cria um dicionario com o ID e o Valor

ID, qtd = map(int, input().split())

preco = produtos[ID] * qtd

print(f"Total: R$ {preco:.2f}")