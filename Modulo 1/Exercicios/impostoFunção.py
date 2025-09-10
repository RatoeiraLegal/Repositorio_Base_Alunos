# Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas

def somaImposto(taxaImposto, custo):
    taxaImposto = (custo * taxaImposto) / 100
    custoFinal = custo + taxaImposto
    print(f"O custo final do produto é: {custoFinal} ")

custo = float(input("Digite o valor do produto: "))
taxaImposto = float(input("Digite o valor da taxa em porcentagem: "))

somaImposto(taxaImposto, custo)