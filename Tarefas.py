#Variáveis do programa:
# Lista_tarefas = []

# Lista = [1,2,4,6]
# Lista[2] = 10

# Dicionario = {"Idade":20,"Altura":190}
# Dicionario["Altura"] = 120

# Tupla = (3,5,7)
# Tupla[1] = 9090

# Lista_tarefas = []
# #var de nome
# Nome = ""
# QuantidadeDeTarefas = 0
# LimiteDeTarefas = 2
# Lista = []

def CriarTarefa(QuantidadeDeTarefas,ListaTarefa):
    ListaTarefa.append({"Id":QuantidadeDeTarefas,"Tarefa":input("Digite a tarefa: "),"Status":"Pendente"})
    return len(ListaTarefa)

# while(QuantidadeDeTarefas<LimiteDeTarefas):
    #print(Lista_tarefas)
def ExibirQtdTarefa(Lista:list, Contador:int):
    """Esta é uma função que exibe 
       a quantidade de tarefas de uma lista.

    Args:
        Lista (list): Recebe uma lista de tarefas
        Contador (int): O contador do fluxo
    """
    print(Lista)
    if len(Lista) > 1:
        print(f"Você tem {Contador} tarefas cadastradas")
    else:
        print(f"Você tem {Contador} tarefa cadastrada")

def ConsultarTarefaPorID(Lista:list,Id:int):
    """Esta função busca a lista e depois retorna o ID - posição tarefa

    Args:
        Lista (list): lista de tarefa
        Id (int): posição da tarefa

    Returns:
        List: retorna uma lista a aprtir do ID.
    """
    return Lista[Id]