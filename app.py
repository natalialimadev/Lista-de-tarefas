#Variáveis do programa:
Lista_tarefas = []

# Lista = [1,2,4,6]
# Lista[2] = 10

# Dicionario = {"Idade":20,"Altura":190}
# Dicionario["Altura"] = 120

# Tupla = (3,5,7)
# Tupla[1] = 9090

Lista_tarefas = []

Nome = ""
QuantidadeDeTarefas = 0
LimiteDeTarefas = 2

#Fim das variáveis.

while(QuantidadeDeTarefas<LimiteDeTarefas):
    #Tarefa = input("Digite a tarefa: ")
    Lista_tarefas.append({"Id":QuantidadeDeTarefas,"Tarefa":input("Digite a tarefa: "),"Status":"Pendente"})
    QuantidadeDeTarefas = len(Lista_tarefas)
    #print(Lista_tarefas)
    
print(Lista_tarefas)
if len(Lista_tarefas) > 1:
    print(f"Você tem {QuantidadeDeTarefas} tarefas cadastradas")
else:
    print(f"Você tem {QuantidadeDeTarefas} tarefa cadastrada")
