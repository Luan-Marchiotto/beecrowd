conector1 = list(map(int, input().split()))
conector2 = list(map(int, input().split()))
contador = 0

for i in range(5):
    if conector1[i] + conector2[i] != 1:
        contador += 1
        break

if contador >= 1:
    print("N")
elif contador == 0:
    print("Y")