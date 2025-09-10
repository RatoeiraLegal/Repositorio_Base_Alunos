# Desenvolva um programa que solicite ao usuário os dados
# de um produto (nome, valor e quantidade) e armazene-os em
# um arquivo de texto chamado "produtos.txt".

nomeP = input("Digite o nome do produto: ")
valor = input("Digite o valor do produto: ")
quantidade = input("Digite a quantidade: ")

with open("produtos.txt", "a") as arquivo:
    arquivo.write(nomeP + " | " + valor + " R$" + " | " + quantidade + "\n")