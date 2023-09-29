# https://realpython.com/prevent-python-sql-injection/


from psycopg2 import Error

from database.conexao_factory import ConexaoFactory


def create_table():
    try:
        conexao_factory = ConexaoFactory()
        conexao = conexao_factory.get_conexao()
        cursor = conexao.cursor()
        query = """
        CREATE TABLE users (
            id INT GENERATED ALWAYS AS IDENTITY,
            username VARCHAR NOT NULL,
            password VARCHAR NOT NULL,
            PRIMARY KEY (id)
        );
        """
        cursor.execute(query)
        conexao.commit()
        print(">>> Table created successfully in PostgreSQL")
    except (Exception, Error) as error:
        print(">>> Error while connecting to PostgreSQL", error)
    finally:
        if conexao:
            cursor.close()
            conexao.close()
            print("[DEBUG] PostgreSQL connection is closed")


def populate_users():
    try:
        conexao_factory = ConexaoFactory()
        conexao = conexao_factory.get_conexao()
        cursor = conexao.cursor()
        query = """
        INSERT INTO
            users (username, "password")
        VALUES
            ('admin', 'admin'),
            ('administrador', 'abracadabra'),
            ('root', 'root');
        """
        cursor.execute(query)
        conexao.commit()
        print(">>> Table users populated")
    except (Exception, Error) as error:
        print(">>> Error while inserting user to table users", error)
    finally:
        if conexao:
            cursor.close()
            conexao.close()
            print("[DEBUG] PostgreSQL connection is closed")


def empty_table():
    try:
        conexao_factory = ConexaoFactory()
        conexao = conexao_factory.get_conexao()
        cursor = conexao.cursor()
        query = "TRUNCATE TABLE users;"
        cursor.execute(query)
        conexao.commit()
        print(">>> Table users cleaned")
    except (Exception, Error) as error:
        print(">>> Error while inserting user to table users", error)
    finally:
        if conexao:
            cursor.close()
            conexao.close()
            print("[DEBUG] PostgreSQL connection is closed")

def escolha_da_query_username(username: str):
    print("""[Username] Escolha uma das seguintes queries:
            1 - "SELECT id FROM users WHERE username = '" + username + "'"
            2 - "SELECT id FROM users WHERE username = '%s'" % username
            3 - "SELECT id FROM users WHERE username = '{}'".format(username)
            4 - f"SELECT id FROM users WHERE username = '{username}'"
            5 - "SELECT id FROM users WHERE username = %s", (username,)
            6 - "SELECT id FROM users WHERE username = %(username)s", {'username': username}
            0 - Voltar ao menu anterior\n
    """)
    escolha = input('Digite a opção: ')

    if escolha == '0':
        return
    if escolha == '1':
        return existe_usuario("SELECT id FROM users WHERE username = '" + username + "'")
    elif escolha == '2':
        return existe_usuario("SELECT id FROM users WHERE username = '%s'" % username)
    elif escolha == '3':
        return existe_usuario("SELECT id FROM users WHERE username = '{}'".format(username))
    elif escolha == '4':
        return existe_usuario(f"SELECT id FROM users WHERE username = '{username}'")
    elif escolha == '5':
        return existe_usuario("SELECT id FROM users WHERE username = %s", (username,))
    elif escolha == '6':
        return existe_usuario("SELECT id FROM users WHERE username = %(username)s", {'username': username})
    else:
        print('Opção inválida! Por favor, tente novamente!')

    escolha_da_query_username(username)


def existe_usuario(*args, **kwargs):
    conexao_factory = ConexaoFactory()
    conexao = conexao_factory.get_conexao()
    cursor = conexao.cursor()
    cursor.execute(*args, **kwargs)
    print(f"[DEBUG] {cursor.query}")
    result = cursor.fetchone()
    cursor.close()
    conexao.close()

    if result is None:
        return False

    return True


def escolha_da_query_senha(senha: str):
    print("""[Username] Escolha uma das seguintes queries:
            1 - "SELECT id FROM users WHERE password = '" + senha + "'"
            2 - "SELECT id FROM users WHERE password = '%s'" % senha
            3 - "SELECT id FROM users WHERE password = '{}'".format(senha)
            4 - f"SELECT id FROM users WHERE password = '{senha}'"
            5 - "SELECT id FROM users WHERE password = %s", (senha,)
            6 - "SELECT id FROM users WHERE password = %(senha)s", {'senha': senha}
            0 - Voltar ao menu anterior\n
    """)
    escolha = input('Digite a opção: ')

    if escolha == '0':
        return
    if escolha == '1':
        return senha_valida("SELECT id FROM users WHERE password = '" + senha + "'")
    elif escolha == '2':
        return senha_valida("SELECT id FROM users WHERE password = '%s'" % senha)
    elif escolha == '3':
        return senha_valida("SELECT id FROM users WHERE password = '{}'".format(senha))
    elif escolha == '4':
        return senha_valida(f"SELECT id FROM users WHERE password = '{senha}'")
    elif escolha == '5':
        return senha_valida("SELECT id FROM users WHERE password = %s", (senha,))
    elif escolha == '6':
        return senha_valida("SELECT id FROM users WHERE password = %(senha)s", {'senha': senha})
    else:
        print('Opção inválida! Por favor, tente novamente!')

    escolha_da_query_username(senha)


def senha_valida(*args, **kwargs):
    conexao_factory = ConexaoFactory()
    conexao = conexao_factory.get_conexao()
    cursor = conexao.cursor()
    cursor.execute(*args, **kwargs)
    print(f"[DEBUG] {cursor.query}")
    result = cursor.fetchone()
    cursor.close()
    conexao.close()

    if result is None:
        return False

    return True

def login():
    username = input('Digite o nome do usuario: ')
    if escolha_da_query_username(username):
        password = input('Digite a senha do usuario: ')
        if escolha_da_query_senha(password):
            print(">>> Login bem sucedido!")
        else:
            print(">>> Falha no login!")
    else:
        print(">>> Usuário não encontrado.")




def menu_principal():
    print('[Menu Principal] Escolha uma das seguintes opções:\n'
            '1 - Criar tabela de usuários\n'
            '2 - Popular a tabela de usuários com alguns registros\n'
            '3 - Login\n'
            '4 - Excluir todos os registros\n'
            '0 - Sair do programa\n')
    escolha = input('Digite a opção: ')

    if escolha == '0':
        print('>>> Obrigado, até logo!')
        return
    if escolha == '1':
        create_table()
    elif escolha == '2':
        populate_users()
    elif escolha == '3':
        login()
    elif escolha == '4':
        empty_table()
    else:
        print('>>> Opção inválida! Por favor, tente novamente!')

    menu_principal()

if __name__ == '__main__':
    print('Bem-vindo a ára Administrativa da Livraria SHIFT - Mastering Python!')
    menu_principal()