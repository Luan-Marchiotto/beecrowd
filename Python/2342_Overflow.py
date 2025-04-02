import re

memoria = int(input())

conta = input()

termos = re.findall(r'\d+', conta)

operadores = re.findall(r'[\+\-\*/]', conta)

termos0 = int(termos[0])
termos1 = int(termos[1])
operador = operadores[0]

if operador == '*':
    conta_final = termos0 * termos1
else:
    conta_final = termos0 + termos1
    
print("OK" if conta_final <= memoria else "OVERFLOW")