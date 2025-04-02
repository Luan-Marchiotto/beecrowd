rep = int(input())

for i in range(rep):
    num = input()
    num = int(num)

    binario = bin(num)[2:]

    print(binario.count("1"))