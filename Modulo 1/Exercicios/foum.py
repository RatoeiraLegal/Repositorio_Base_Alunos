#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

valor = input("Digite M ou F: ")
if valor == "M":
    print("Masculino")
elif valor == "F":
    print("Feminino")
else:
    print("Sexo Inválido")