import time

rep = int(input())


for i in range(rep):
    inicio = time.time()
    texto = input()
    fim = time.time()

    tempo_gasto = fim - inicio

    print(f"{tempo_gasto:.2f}")