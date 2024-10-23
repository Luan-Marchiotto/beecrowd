valorNotas = int(input())

atual = valorNotas

notas100 = atual // 100 # O // usa a divisão inteira
atual -= notas100 * 100

notas50 = atual // 50  
atual -= notas50 * 50

notas20 = atual // 20 
atual -= notas20 * 20

notas10 = atual // 10 
atual -= notas10 * 10

notas5 = atual // 5 
atual -= notas5 * 5

notas2 = atual // 2
atual -= notas2 * 2

notas1 = atual

print(valorNotas)
print(f'{notas100} nota(s) de R$ 100,00')
print(f'{notas50} nota(s) de R$ 50,00')
print(f'{notas20} nota(s) de R$ 20,00')
print(f'{notas10} nota(s) de R$ 10,00')
print(f'{notas5} nota(s) de R$ 5,00')
print(f'{notas2} nota(s) de R$ 2,00')
print(f'{notas1} nota(s) de R$ 1,00')