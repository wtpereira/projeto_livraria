from model.categoria import Categoria
from database.conexao_factory import ConexaoFactory

class CategoriaDAO:

    def __init__(self):
        self.__conexao_factory = ConexaoFactory()
        self.__categorias: list[Categoria] = list()

    def listar(self) -> list[Categoria]:
        categorias = list()
        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT id, nome FROM categorias")
        resultados = cursor.fetchall()
        for resultado in resultados:
            cat = Categoria(resultado[1], resultado[0])
            categorias.append(cat)

        cursor.close()
        conexao.close()
        return categorias

    def adicionar(self, categoria: Categoria) -> None:
        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute(f"INSERT INTO categorias (nome) VALUES ('{categoria.nome}')")
        conexao.commit()
        cursor.close()
        conexao.close()

    def remover(self, categoria_id: int) -> bool:
        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM categorias WHERE id = %s", (categoria_id,))
        categorias_removidas = cursor.rowcount
        conexao.commit()
        cursor.close()
        conexao.close()

        if (categorias_removidas == 0):
            return False

        return True

    def buscar_por_id(self, categoria_id) -> Categoria:
        cat = None
        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT id, nome FROM categorias WHERE id = %s", (categoria_id,))
        resultado = cursor.fetchone()
        if (resultado):
            cat = Categoria(resultado[1], resultado[0])

        cursor.close()
        conexao.close()
        return cat
