x = int(input())
z = int(input())

while z <= x:
    z = int(input())

soma = 0
cont = 0

while soma <= z:
    soma += x
    x += 1
    cont += 1

print(cont)