cont = 0
total = 0

while True:
    try:
        acao, passageiros = input().split()
        passageiros = int(passageiros)
    except ValueError:
        break

    if acao == 'SALIDA':
        total -= passageiros
        cont += 1
    elif acao == 'VUELTA':
        total += passageiros
        cont -= 1
    else:
        break 

print(abs(total))
print(abs(cont))