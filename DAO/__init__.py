import psycopg2
# Estabelecendo a conexão com o Banco de dados
def conectardb():
    conexao = psycopg2.connect(database="minicurso_db",
                               host="localhost",
                               user="postgres",
                               password="1234",
                               port="5432")
    #print("Conexão realizada com sucesso!")
    return conexao

# Chame a função para testar a conexão
conexao = conectardb()


def inserir_usuario(nome, email):
    conexao = conectardb()                 # Estabelece conexão com o banco de dados.
    cursor = conexao.cursor()             # Cria um cursor para executar comandos SQL.
    cursor.execute("INSERT INTO usuarios (nome, email) VALUES (%s, %s)", (nome, email))
                                       # Executa o comando INSERT para adicionar um novo usuário.
    conexao.commit()                      # Salva (confirma) a transação no banco de dados.
    cursor.close()                        # Fecha o cursor.
    conexao.close()                       # Fecha a conexão com o banco de dados.


# def buscar_usuario(nome):
#    conexao = conectardb()                  # Conecta ao banco.
#    cursor = conexao.cursor()             # Cria um cursor para consultas.
    cursor.execute(f"SELECT email,nome FROM usuarios where nome= '{nome}' ")
                                         # Executa o comando SELECT para obter todos os usuários.
    resultado = cursor.fetchall()         # Recupera todos os resultados da consulta em uma lista.
    cursor.close()                        # Fecha o cursor.
    conexao.close()                       # Fecha a conexão com o banco.
    return resultado                      # Retorna a lista de usuários.

#Listar Todos Usuários
def listar_usuarios():
    conexao = conectardb()                  # Conecta ao banco.
    cursor = conexao.cursor()             # Cria um cursor para consultas.
    cursor.execute(f"SELECT email,nome FROM usuarios")
                                         # Executa o comando SELECT para obter todos os usuários.
    resultado = cursor.fetchall()         # Recupera todos os resultados da consulta em uma lista.
    cursor.close()                        # Fecha o cursor.
    conexao.close()                       # Fecha a conexão com o banco.
    return resultado                      # Retorna a lista de usuários.

#Atualizar Usuário
def atualizar_usuario(id, novo_nome, novo_email):
    conexao = conectardb()                  # Conecta ao banco.
    cursor = conexao.cursor()             # Cria um cursor para o comando de atualização.
    cursor.execute("UPDATE usuarios SET nome = %s, email = %s WHERE id = %s", (novo_nome, novo_email, id))
                                         # Atualiza o nome e email do usuário com o id especificado.
    conexao.commit()                      # Salva a transação.
    cursor.close()                        # Fecha o cursor.
    conexao.close()                       # Fecha a conexão com o banco.]
    return buscar_usuario_id(56)

#Deletar Usuário
def deletar_usuario(id):
    conexao = conectardb()                  # Conecta ao banco.
    cursor = conexao.cursor()             # Cria um cursor para o comando de exclusão.
    cursor.execute("DELETE FROM usuarios WHERE id = %s", (id,))
                                         # Executa o comando DELETE para remover o usuário com o id dado.
    conexao.commit()                      # Salva a transação.
    cursor.close()                        # Fecha o cursor.
