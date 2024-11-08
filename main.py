import DAO

# Teste de inserção
#DAO.inserir_usuario('Jose', 'jose@teste.com.br')
#DAO.inserir_usuario('Maria', 'maira@teste.com.br')
#DAO.inserir_usuario('Fabio', 'fabio@teste.com.br')

# Teste de consulta
#saida = DAO.buscar_usuario('Fabio')
#print(saida)

# Teste de listar todos
saida = DAO.listar_usuarios()
print(saida)

# Teste de atualização
#saida = DAO.atualizar_usuario('amanda','teste@teste.com')

# Teste de remoção
# saida = DAO.deletar_usuario('amanda@amanda.com')
#print(saida)

#DAO.inserir_usuario(nome)

#DAO.atualizar_usuario(id, novo_nome, novo_email)

#DAO.deletar_usuario(id)