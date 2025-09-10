# arquivo = open('lista_de_compras.csv', "w", newline='')
# arquivo_write = csv.writer(arquivo, delimiter=' ')
# arquivo_write.writerow(['Frutas:','maçãs','bananas','morangos'])
# arquivo_write.writerow(['Laticínios:','leite','queijo','iogute'])
# arquivo_write.writerow(['Limpeza:','sabão','detergente','esponja'])
import csv
import os

lista = []
while True:
    escolha = int(input("1. Adicionar produto \n2. Sair \nEscolha: "))
    if escolha == 2:
        break
    elif escolha == 1:
        produto = input("Digite o nome do produto: ")
        topico = input(f"Digite o topico do produto '{produto}': ")
        lista.append({'Topico': topico, 'Produto': produto})
    else:
        print("Valor inválido!")


existe = os.path.isfile('lista_de_compras.csv')

with open('lista_de_compras.csv', "a", newline='') as arquivo:
    colunas = ['Topico', 'Produto']
    arquivo_write = csv.DictWriter(arquivo, fieldnames = colunas, delimiter='\t')
    if not existe:
        arquivo_write.writeheader()
    arquivo_write.writerows(lista)


# arquivo_write.writerow([topico, produto])



