rep = int(input())

for _ in range(rep):
    pop_a, pop_b, cres_1, cres_2 = input().split()
    pop_a = int(pop_a)
    pop_b = int(pop_b)
    cres_1 = float(cres_1)
    cres_2 = float(cres_2)
    
    anos = 0

    while pop_a <= pop_b:
        pop_a += int(pop_a * (cres_1 / 100))
        pop_b += int(pop_b * (cres_2 / 100))
        anos += 1

        if anos > 100:
            print("Mais de 1 seculo.")
            break
    
    if anos <= 100:
        print(f"{anos} anos.")