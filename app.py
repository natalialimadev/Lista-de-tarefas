from Tarefas import CriarTarefa
QtdTarefa = 0
ListaDeTarefas = []
#Fim das variáveis.
while(True):
    Acao = input("O que você quer fazer? ")
    # print(Acao)
    # print(Acao.lower())
    if Acao.lower() == "criar":
        print("Criando uma tarefa")
        CriarTarefa(QtdTarefa,ListaDeTarefas)

    elif Acao.lower() == "detalhe":
        print("Consultando tarefa")
    elif Acao.lower() == "sair":
        print("Você saiu")
        break
    else: 
        print("Digite uma ação válida ")


