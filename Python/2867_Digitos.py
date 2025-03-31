rep = int(input())

for i in range(rep):
    a, b = map(int, input().split())
    
    valor = str(pow(a, b))
    
    print(len(valor))