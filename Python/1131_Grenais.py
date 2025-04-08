gol1, gol2 = map(int,input().split())
qtd_grenais = 1

inter = 0
gremio = 0
empate = 0

if gol1 > gol2:
    inter += 1
elif gol2 > gol1:
    gremio += 1
elif gol1 == gol2:
    empate += 1

while True:
    print("Novo grenal (1-sim 2-nao)")
    choise = int(input())
    
    if choise == 2:
        break
    else:
        gol1, gol2 = map(int,input().split())
        
        if gol1 > gol2:
            inter += 1
        elif gol2 > gol1:
            gremio += 1
        elif gol1 == gol2:
            empate += 1
            
        qtd_grenais += 1

print(f"{qtd_grenais} grenais")
print(f"Inter:{inter}")
print(f"Gremio:{gremio}")
print(f"Empates:{empate}")

if inter > gremio:
    print("Inter venceu mais")
elif gremio > inter:
    print("Gremio venceu mais")
elif inter == gremio:
    print("Nao houve vencedor")