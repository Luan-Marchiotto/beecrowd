bolinhas = int(input())
galhos = int(input())

diferenca = round(galhos / 2)

if(bolinhas >= galhos or diferenca < bolinhas):

	print("Amelia tem todas bolinhas!")

elif(diferenca > bolinhas):

	difGalhos = round(galhos / 2)

	diferenca = difGalhos - bolinhas

	print(f"Faltam {diferenca} bolinha(s)")
 
else:
	print("Amelia tem todas bolinhas!")