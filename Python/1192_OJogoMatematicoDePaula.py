rep = int(input())

for _ in range(rep):
    texto = input()
    
    for i in texto:
        if i.isalpha():
            partes = texto.split(i)
            
            num1 = int(partes[0])
            num2 = int(partes[1])

            if i.isupper():
                if num1 == num2:
                    soma = num1 * num2
                else:
                    soma = num2 - num1
            elif i.islower():
                if num1 == num2:
                    soma = num1 * num2
                else:
                    soma = num1 + num2
    print(soma)