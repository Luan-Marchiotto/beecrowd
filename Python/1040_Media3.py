N1, N2, N3, N4 = map(float, input().split())

nota_exame = 0.0

media = ((N1*2)+(N2*3)+(N3*4)+(N4*1))/10

print(f'Media: {media:.1f}')

if(media >= 7.0):
    print("Aluno aprovado.")

if(media < 5.0):
    print("Aluno reprovado.")

if(media >= 5.0 and media <= 6.9):
    print("Aluno em exame.")

    nota_exame = float(input())

    print(f"Nota do exame: {nota_exame:.1f}")

    media = (media + nota_exame)/2
    
    if(media >= 5.0):
        print("Aluno aprovado.")

    else:
        print("Aluno reprovado.")
        
    print(f'Media final: {media:.1f}')