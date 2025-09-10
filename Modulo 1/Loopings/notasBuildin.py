lista = []

nome = input("Digite seu nome: ")
repetidor = 1
while repetidor <=4:
    notas = int(input(f"Digite a {repetidor}º nota: "))
    lista.append(notas)
    repetidor += 1

print()
print(f"Notas: {lista}")
média = (sum(lista))/4
print(f"Média: {média}")
notas = str(lista)
média = str(média)

with open("notas.txt", "a") as arquivo:
    arquivo.write(nome + " | Notas: " + notas + " | Média: " + média + "\n")
