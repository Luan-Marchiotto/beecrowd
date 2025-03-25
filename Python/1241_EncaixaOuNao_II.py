rep = int(input())

for i in range(rep):
    A, B = input().split()
    
    A_int = int(A)
    B_int = int(B)
    
    if B_int > A_int:
        print("nao encaixa")
        
    elif B_int < A_int:
        tamanho_B = len(B)
        ultimos_A = A[-tamanho_B:]
        
        if ultimos_A == B:
            print("encaixa")
        else:
            print("nao encaixa")
    else:
        print("encaixa")