with open("dados.txt", "r") as arquivo:
    dados = arquivo.readlines()
    linhas = len(dados)
    repetidor = 0
    linharepetidor = 1
    while repetidor < linhas:
        print(f"Linha {linharepetidor}: {dados[repetidor]}")
        repetidor += 1
        linharepetidor += 1