with open("dados.txt", "r") as arquivo:
    dados = arquivo.read()
    
with open("copia_dados.txt", "a") as copia:
    copia.write(dados)