cont_par = 0
cont_impar = 0
cont_positivo = 0
cont_negativo = 0

for _ in range(5):
    x = int(input())
    
    # Par ou ímpar
    if x % 2 == 0:
        cont_par += 1
    else:
        cont_impar += 1
        
    # Positivo ou negativo
    if x > 0:
        cont_positivo += 1
    elif x < 0:
        cont_negativo += 1

print(f'{cont_par} valor(es) par(es)')
print(f'{cont_impar} valor(es) impar(es)')
print(f'{cont_positivo} valor(es) positivo(s)')
print(f'{cont_negativo} valor(es) negativo(s)')