nome = input()
salfixo = float(input())
qtdDeVendas = float(input())

bonus = float(qtdDeVendas * (15/100))

total = salfixo + bonus

print(f"TOTAL = R$ {total:.2f}")