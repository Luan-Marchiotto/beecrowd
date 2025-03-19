while True:

    
    n = int(input())
    
    if n == 0:
        break
    
    vitamina = {
        'suco de laranja': 120,
        'morango fresco': 85,
        'mamao': 85,
        'goiaba vermelha': 70,
        'manga': 56,
        'laranja': 50,
        'brocolis': 34
    }
    
    soma_total = 0 

    for i in range(n):
        quantidade, produto = input().split(maxsplit=1)
        quantidade = int(quantidade)
        
        if produto in vitamina:
            soma_total += vitamina[produto] * quantidade
            
    limite_inferior = 110
    limite_superior = 130

    if soma_total < limite_inferior:
        print(f"Mais {limite_inferior - soma_total} mg")
    elif soma_total > limite_superior:
        print(f"Menos {soma_total - limite_superior} mg")
    else:
        print(f"{soma_total} mg")
