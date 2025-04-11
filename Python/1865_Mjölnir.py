rep = int(input())

for _ in range(rep):
    nome, forca = input().split()
    
    forca = int(forca)
    
    if nome == 'Thor':
        print("Y")
    else:
        print("N")