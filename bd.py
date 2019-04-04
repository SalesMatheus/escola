# Função validar login
def get_idlogin(cursor, login, senha):
    # Executar o sql
    cursor.execute(f'select idlogin from login where login = "{login}" and senha = "{senha}"')

    # Recuperando o retorno do BD
    idlogin = cursor.fetchone()

    # Fechar o cursor
    cursor.close()

    # Retornar o idlogin
    return idlogin[0]

# Funcao para retornar as disciplinas
def get_notas(cursor, idlogin):
    # Executar o SQL
    cursor.execute(f'select disciplinas.nome, disciplinas.iddisciplinas, notas.nota1, notas.nota2, notas.nota3 from notas, disciplinas where disciplinas.iddisciplinas = notas.iddisciplinas and notas.id_login  =  {idlogin}')

    # Recuperando o retorno do BD
    disciplinas = cursor.fetchall()

    # Fechar o cursor
    cursor.close()

    # Retornar os dados
    return disciplinas

# Funcao para retornar as disciplinas
def get_descricao(cursor, disciplina):
    # Executar o SQL
    cursor.execute(f'select descricao from  disciplinas where iddisciplinas  =  {disciplina}')

    # Recuperando o retorno do BD
    descricao = cursor.fetchone()

    # Fechar o cursor
    cursor.close()

    # Retornar os dados
    return descricao


