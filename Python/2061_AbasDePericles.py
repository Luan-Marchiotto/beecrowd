abas, quantidade = map(int,input().split())

for _ in range(quantidade):
    
    acao = input()
    
    if acao == "fechou":
        abas += 1
    elif acao == "clicou":
        abas -= 1
    
print(abas)