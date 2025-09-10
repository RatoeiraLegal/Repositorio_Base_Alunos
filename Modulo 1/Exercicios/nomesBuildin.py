
repetidor = 1
while repetidor <= 5:
    nome = input(f"Digite o {repetidor}º nome: ")
    nomes += [nome]
    repetidor += 1


with open("nomes.txt", "a") as arquivo:
    arquivo.write(str(nomes))