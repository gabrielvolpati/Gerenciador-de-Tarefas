from rich import print
from rich.table import Table
import json

class Tarefa:
    def __init__(self, id_tarefa, titulo, descricao):
        if not titulo.strip():
            raise ValueError("O título não pode estar vazio!")

        self.id = id_tarefa
        self.titulo = titulo
        self.descricao = descricao
        self.concluida = False

    def concluir(self):
        # muda o status para concluída.
        self.concluida = True

    def to_dict(self):
        # converte o objeto em dicionário para salvar no JSON.
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "concluida": self.concluida
        }


class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []
        self.carregar_tarefas()

    def adicionar_tarefa(self, titulo, descricao):
        ids = []
        for tarefa in self.tarefas:
            ids.append(tarefa.id)

        if not ids:
            novo_id = 1

        else:
            novo_id = max(ids) + 1

        tarefa = Tarefa(novo_id, titulo, descricao)
        self.tarefas.append(tarefa)

        self.salvar_tarefas()

    def listar_tarefas(self):
        if not self.tarefas:
            print("Nenhuma tarefa foi adicionada ainda.")

        else:
            tabela = Table(title=("Tarefas"))

            tabela.add_column("ID", justify="left", style="red")
            tabela.add_column("Título", justify="center", style="blue")
            tabela.add_column("Descrição", justify="center", style="blue")
            tabela.add_column("Status", justify="center", style="blue")
            for tarefa in self.tarefas:
                tabela.add_row(f"{tarefa.id}", f"{tarefa.titulo}", f"{tarefa.descricao}", f"{tarefa.concluida}")
            print(tabela)

    def buscar_tarefa_por_id(self, id_tarefa):
        for tarefa in self.tarefas:
            if tarefa.id == id_tarefa:
                return tarefa

        return None


    def concluir_tarefa(self, id_tarefa):

        tarefa = self.buscar_tarefa_por_id(id_tarefa)

        if tarefa is None:
            raise ValueError("Nenhuma tarefa encontrada com esse ID.")

        if tarefa.concluida:
            print("Essa tarefa já está concluída.")
            return

        tarefa.concluir()
        print(f"Tarefa '{tarefa.titulo}' concluída com sucesso!")

        self.salvar_tarefas()


    def excluir_tarefa(self, id_tarefa):

        tarefa = self.buscar_tarefa_por_id(id_tarefa)

        if tarefa is None:
            raise ValueError("Nnehum tarefa encontrada com esse ID.")

        self.tarefas.remove(tarefa)
        print(f"Tarefa '{tarefa.titulo}' excluída com sucesso!")

        self.salvar_tarefas()

    def salvar_tarefas(self):
        dados = []
        for tarefa in self.tarefas:
            dados.append(tarefa.to_dict())

        with open("tarefas.json", "w", encoding = "utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)

    def carregar_tarefas(self):
        try:
            with open("tarefas.json", "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)

        except FileNotFoundError:
            return

        for dado in dados:
            tarefa = Tarefa(
                dado["id"],
                dado["titulo"],
                dado["descricao"]
            )

            tarefa.concluida = dado["concluida"]

            self.tarefas.append(tarefa)

    def mostrar_tarefa_por_id(self, id_tarefa):

        tarefa = self.buscar_tarefa_por_id(id_tarefa)

        if tarefa is None:
            print("Nenhuma tarefa com esse ID foi encontrada.")
            return

        tabela = Table(title=f"Tarefa {id_tarefa}")

        tabela.add_column("ID", style="red")
        tabela.add_column("Título", style="blue")
        tabela.add_column("Descrição", style="blue")
        tabela.add_column("Status", style="blue")

        status = "Concluída" if tarefa.concluida else "Pendente"

        tabela.add_row(
            str(tarefa.id),
            tarefa.titulo,
            tarefa.descricao,
            status
        )

        print(tabela)
