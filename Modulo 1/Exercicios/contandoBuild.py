with open("dados.txt", "r") as arquivo:
    dados = arquivo.readlines()
    quantidade = len(dados)
    print(quantidade)