tipo = input()
jeito = input()
modelo = input()

if(tipo == 'vertebrado'):
    if(jeito == 'ave'):
        if(modelo == 'carnivoro'):
            print("aguia")
        else:
            print("pomba")
    elif(jeito == 'mamifero'):
        if(modelo == 'onivoro'):
            print("homem")
        else:
            print("vaca")
else:
    if(jeito == 'inseto'):
        if(modelo == 'hematofago'):
            print("pulga")
        else:
            print("lagarta")
    elif(jeito == 'anelideo'):
        if(modelo == 'hematofago'):
            print("sanguessuga")
        else:
            print("minhoca")