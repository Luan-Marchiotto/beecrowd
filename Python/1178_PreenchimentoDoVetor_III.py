X = float(input())

N = []

for i in range(100):
    N.append(X)
    
    print(f'N[{i}] = {X:.4f}')
    
    X /= 2