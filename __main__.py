from Classes import GerenciadorTarefas
from rich import print
from rich.panel import Panel
from rich.table import Table
from rich.traceback import install

install()


def main():
    gerenciador = GerenciadorTarefas()

    while True:
        caixa = Panel(""
                      "[bright_white]1 - Adicionar tarefa\n"
                      "2 - Listar tarefas\n"
                      "3 - Concluir Tarefa\n"
                      "4 - Excluir tarefa\n"
                      "5 - Mostrar tarefa por ID\n"
                      "6 - Sair[/]", title="GERENCIADOR DE TAREFAS", style="green", width=36)
        print(caixa)
        escolha = input("Escolha o que deseja: ")

        match escolha:

            case "1":
                titulo = input("Título: ")
                descricao = input("Descrição: ")

                try:
                    gerenciador.adicionar_tarefa(titulo, descricao)
                    print("Tarefa adicionada com sucesso!")

                except ValueError as erro:
                    print(f"Erro: {erro}")

            case "2":
                gerenciador.listar_tarefas()

            case "3":

                try:
                    id_tarefa = int(input("Digite o ID da tarefa que será concluída: "))
                    gerenciador.concluir_tarefa(id_tarefa)


                except ValueError as erro:
                    print(f"Erro: {erro}")

            case "4":
                try:
                    id_tarefa = int(input("Digite o ID da tarefa que será excluída: "))
                    gerenciador.excluir_tarefa(id_tarefa)

                except ValueError as erro:
                    print(f"Erro: {erro}")

            case "5":
                try:
                    id_tarefa = int(input("Digite o ID da tarefa que será buscada: "))
                    gerenciador.mostrar_tarefa_por_id(id_tarefa)

                except ValueError:
                    print("Digite um ID numérico.")
                break



if __name__ == "__main__":
    main()
