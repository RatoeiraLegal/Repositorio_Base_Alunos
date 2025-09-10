# Desafio 1: Gerenciador de Tarefas Simples
# Objetivo: Criar um programa que permita ao usuário adicionar, visualizar e marcar tarefas como concluídas.
# Descrição:
#  Você vai desenvolver um gerenciador de tarefas usando listas e dicionários. O programa deve:
# Permitir adicionar tarefas (com nome e descrição).
# Mostrar todas as tarefas não concluídas.
# Marcar tarefas como "concluídas" (alterando seu status).
# Opcional: Salvar as tarefas em um arquivo .txt para não perder ao fechar o programa.
# Habilidades praticadas:
# Listas e dicionários.
# Estruturas de repetição (while, for).
# Funções básicas (ex: adicionar_tarefa(), mostrar_tarefas()).
# Manipulação de arquivos (opcional).

dados = []
try:
    with open("tarefas.txt", "r") as arquivo:
        conteudo = arquivo.readlines()
        x = len(conteudo)
        repetidor = 0
        while repetidor < x:
            nome = str(conteudo[repetidor].split(" ")[0])
            descricao = str(conteudo[repetidor].split(" ")[3])
            status = str(conteudo[repetidor].split(" ")[4])
            tarefa = {"tarefa":nome, "descrição":descricao, "status":status}
            dados.append(tarefa)
            repetidor += 1
except:
    pass


def adicionar():
    nome = input("Digite o nome da tarefa: ")
    descricao = input("Digite a descrição: ")
    status = "pendente"
    tarefa = {"tarefa":nome, "descrição":descricao, "status":status}
    dados.append(tarefa)

def visualizar(dados):
    repetidor1 = 0
    quantidade = len(dados)
    while repetidor1 < quantidade:
        if dados[repetidor1]["status"] == "pendente":
            print(f'{dados[repetidor1]["tarefa"]} - Descrição: {dados[repetidor1]["descrição"]} [{dados[repetidor1]["status"]}]')
        repetidor1 += 1
    repetidor1 = 0
    while repetidor1 < quantidade:
        if dados[repetidor1]["status"] == "concluído":
            print(f'{dados[repetidor1]["tarefa"]} - Descrição: {dados[repetidor1]["descrição"]} [{dados[repetidor1]["status"]}]')
        repetidor1 += 1
        
    
def alterar():
    nomeT = input("Digite o nome da tarefa: ")
    repetidor2 = 0
    quantidade = len(dados)
    while repetidor2 < quantidade:
        if nomeT == dados[repetidor2]["tarefa"]:
            dados[repetidor2]["status"] = "concluído"
            print("Alterado com sucesso!")
            return
        repetidor2 += 1
        
while True:
    print()
    menu = int(input(f"1.Adicionar Tarefa\n2.Visualizar Tarefas\n3.Alterar status\n4.Finalizar programa\nEscolha: "))
    if menu == 1:
        print()
        adicionar()
    elif menu == 2:
        print()
        visualizar(dados)
    elif menu == 3:
        print()
        alterar()
    elif menu == 4:
        print("Finalizando...")
        break 
    else:
        print("Valor inválido!")

with open ("tarefas.txt", "w") as arquivo:
    repetidor4 = 0
    while repetidor4 < len(dados):
        linha = (f'{dados[repetidor4]["tarefa"]} - Descrição: {dados[repetidor4]["descrição"]} {dados[repetidor4]["status"]}'' ''\n')
        arquivo.write(linha)
        repetidor4 += 1