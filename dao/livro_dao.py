from model.livro import Livro
from model.categoria import Categoria
from database.conexao_factory import ConexaoFactory
from dao.categoria_dao import CategoriaDAO
from dao.editora_dao import EditoraDAO
from dao.autor_dao import AutorDAO


class LivroDAO:

    def __init__(self):
        self.__conexao_factory = ConexaoFactory()

    def listar(self) -> list[Livro]:
        livros = list()
        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT titulo, resumo, ano, paginas, isbn, categoria_id, editora_id, autor_id, id FROM livros")
        resultados = cursor.fetchall()
        for resultado in resultados:
            categoria = CategoriaDAO().buscar_por_id(resultado[5])
            editora = EditoraDAO().buscar_por_id(resultado[6])
            autor = AutorDAO().buscar_por_id(resultado[7])
            livro = Livro(resultado[0], resultado[1], resultado[2], resultado[3], resultado[4], categoria, editora, autor, resultado[8])
            livros.append(livro)

        cursor.close()
        conexao.close()
        return livros

    def adicionar(self, livro: Livro) -> None:
        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute(f"INSERT INTO livros (titulo, isbn, paginas, ano, resumo, categoria_id, editora_id, autor_id) VALUES \
                       ('{livro.titulo}', '{livro.isbn}', '{livro.paginas}', '{livro.ano}', '{livro.resumo}', '{livro.categoria.id}', '{livro.editora.id}', '{livro.autor.id}')")
        conexao.commit()
        cursor.close()
        conexao.close()

    def remover(self, livro_id: int) -> bool:
        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM livros WHERE id = %s", (livro_id,))
        livros_removidos = cursor.rowcount
        conexao.commit()
        cursor.close()
        conexao.close()

        if (livros_removidos == 0):
            return False

        return True

    def buscar_por_id(self, livro_id) -> Livro:
        livro = None
        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT titulo, isbn, paginas, ano, resumo, categoria_id, editora_id, autor_id, id FROM livros WHERE id = %s", (livro_id,))
        resultado = cursor.fetchone()
        if (resultado):
            categoria = CategoriaDAO().buscar_por_id(resultado[5])
            editora = EditoraDAO().buscar_por_id(resultado[6])
            autor = AutorDAO().buscar_por_id(resultado[7])
            livro = Livro(resultado[0], resultado[1], resultado[2], resultado[3], resultado[4], categoria, editora, autor, resultado[8])

        cursor.close()
        conexao.close()
        return livro
