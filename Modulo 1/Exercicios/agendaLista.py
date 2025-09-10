contatos = []

while True:
    print()
    escolha = int(input("[1] Cadastrar pessoa \n[2] Listar pessoas \n[3] Excluir pessoa \n[0] Encerrar o programa \nOpção: "))
    print()
    if escolha == 1:
        novaPessoa = input("Digite o nome da pessoa: ")
        contatos.append(novaPessoa)
    elif escolha == 2:
        print(contatos)
    elif escolha == 3:
        removerPessoa = input("Digite o nome da pessoa a ser removida: ")
        contatos.remove(removerPessoa)
        print(f"{removerPessoa} foi removido")
    elif escolha == 0:
        break
    else:
        print("Valor inválido")


