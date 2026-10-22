import mysql.connector
from mysql.connector import cursor

def conectar_banco():
    conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="gerenciador_tarefas"
)

    return conexao

def inserir_tarefa(titulo, descricao):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    sql = """
        INSERT INTO tarefas (titulo, descricao)
        VALUES (%s, %s)
"""

    valores = titulo, descricao

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()

def listar_tarefas():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    sql = """
        SELECT * FROM tarefas
    """

    cursor.execute(sql)

    tarefas = cursor.fetchall()

    cursor.close()
    conexao.close()

    return tarefas



def buscar_tarefa_por_id(id_tarefa):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    sql = """
        SELECT * FROM tarefas
        WHERE id = %s
"""

    valores = (id_tarefa,)

    cursor.execute(sql, valores)

    tarefas = cursor.fetchone()

    cursor.close()
    conexao.close()

    return tarefas


def concluir_tarefa(id_tarefa):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    sql = """
        UPDATE tarefas
        SET concluido = TRUE
        WHERE id = %s
"""

    valores = (id_tarefa,)

    cursor.execute(sql, valores)
    conexao.commit()

    tarefa_alterada = cursor.rowcount

    cursor.close()
    conexao.close()

    return tarefa_alterada

    
def excluir_tarefa(id_tarefa):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    sql = """
        DELETE FROM tarefas
        WHERE id = %s
"""

    valores = (id_tarefa,)

    cursor.execute(sql, valores)
    conexao.commit()

    tarefa_excluida = cursor.rowcount

    cursor.close()
    conexao.close()

    return tarefa_excluida




