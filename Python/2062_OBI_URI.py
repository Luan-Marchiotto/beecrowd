rep = int(input())
texto = input().split()

for ind, i in enumerate(texto):
    
    if(i[0:2]=='UR' and len(i)==3):
        texto[ind] = 'URI'
        
    if(i[0:2]=='OB' and len(i)==3):
        texto[ind] = 'OBI'
        
i = ' '.join(texto)

print(i)