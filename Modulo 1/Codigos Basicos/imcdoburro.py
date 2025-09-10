#Dados do IMC#

peso = int(input("Fala teu peso em quilos: "))
altura = float(input("Fala tua altura em metros: "))

#Cálculo
IMC = float(peso / (altura * altura))

print(IMC)