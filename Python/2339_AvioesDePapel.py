compe, comprada, pedida = map(int,input().split())

if compe * pedida <= comprada:
    print("S")
else:
    print("N")