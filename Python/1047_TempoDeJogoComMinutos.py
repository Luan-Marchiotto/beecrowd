h1, m1, h2, m2 = map(int,input().split())

if h2 <= h1 and m2 <= m1:
    h2 += 24
elif m2 <= m1:
    m2 += 60
    h2 -= 1

soma1 = (h1 * 3600) + (m1 * 60)
soma2 = (h2 * 3600) + (m2 * 60)

tempo = soma2 - soma1

hora  = int(tempo / 3600)

minuto = int((tempo - (hora * 3600)) / 60)

print(f"O JOGO DUROU {hora} HORA(S) E {minuto} MINUTO(S)")