#Variáveis do programa:
Tarefas = []
Nome = ""
QuantidadeDeTarefas = 0
LimiteDeTarefas = 2

#Fim das variáveis.

while(QuantidadeDeTarefas<LimiteDeTarefas):
    Tarefa = input("Digite a tarefa: ")
    Tarefas.append(Tarefa)
    print(Tarefas)
    QuantidadeDeTarefas = len(Tarefas)

if QuantidadeDeTarefas > 1:
    print(f"Você tem {QuantidadeDeTarefas} tarefas cadastradas")
else:
    print(f"Você tem {QuantidadeDeTarefas} tarefa cadastrada")
