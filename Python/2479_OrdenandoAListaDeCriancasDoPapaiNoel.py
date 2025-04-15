rep = int(input())

nomes = []
lista_limpa = []

comportadas = 0
descomportadas = 0

for _ in range(rep):
    nome = input()
    nomes.append(nome)
    
    if nome.startswith('+'):
        comportadas += 1
    elif nome.startswith('-'):
        descomportadas += 1

for n in nomes:
    nome_limpo = n.replace("+ ", "").replace("- ", "")
    lista_limpa.append(nome_limpo)
    
lista_limpa.sort()

for nome in lista_limpa:
    print(nome)

print(f"Se comportaram: {comportadas} | Nao se comportaram: {descomportadas}")