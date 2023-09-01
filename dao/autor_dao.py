from model.autor import Autor
from database.conexao_factory import ConexaoFactory

class AutorDAO:

    def __init__(self):
        self.__conexao_factory = ConexaoFactory()

    def listar(self) -> list[Autor]:
        autores = list()
        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT nome, email, telefone, bio, id FROM autores")
        resultados = cursor.fetchall()
        for resultado in resultados:
            autor = Autor(resultado[0], resultado[1], resultado[2], resultado[3], resultado[4])
            autores.append(autor)

        cursor.close()
        conexao.close()
        return autores


    def adicionar(self, autor: Autor) -> None:
        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute(f"INSERT INTO autores (nome, email, telefone, bio) VALUES \
            ('{autor.nome}', '{autor.email}', '{autor.telefone}', '{autor.bio}')")
        conexao.commit()
        cursor.close()
        conexao.close()

    def remover(self, autor_id: int) -> bool:
        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM autores WHERE id = %s", (autor_id,))
        autores_removidos = cursor.rowcount
        conexao.commit()
        cursor.close()
        conexao.close()

        if (autores_removidos == 0):
            return False

        return True

    def buscar_por_id(self, autor_id) -> Autor:
        autor = None
        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT nome, email, telefone, bio, id FROM autores WHERE id = %s", (autor_id,))
        resultado = cursor.fetchone()
        if (resultado):
            autor = Autor(resultado[0], resultado[1], resultado[2], resultado[3], resultado[4])

        cursor.close()
        conexao.close()
        return autor
