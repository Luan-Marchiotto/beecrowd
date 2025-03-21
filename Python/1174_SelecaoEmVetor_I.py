A = []

for i in range(100):
    x = float(input())
    
    A.append(x)
    
    if x <= 10: 
        print(f"A[{i}] = {x:.1f}")