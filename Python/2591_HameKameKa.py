rep = int(input())
while rep > 0:
    rep -= 1
    
    texto = input().split('me')
    
    primeira_parte = texto[0].count('a')
    segunda_parte = texto[1].count('a')
    
    a = (primeira_parte * segunda_parte) * 'a'
    
    print(f'k{a}')