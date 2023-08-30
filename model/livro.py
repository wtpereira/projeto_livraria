from model.categoria import Categoria
from model.editora import Editora
from model.autor import Autor

class Livro:

    def __init__(self, id: int, titulo: str, resumo: str, ano: int, paginas: int, isbn: str, categoria: Categoria, editora: Editora, autor: Autor):
        self.__id: int = id
        self.__titulo: str = titulo
        self.__resumo: str = resumo
        self.__ano: int = ano
        self.__paginas: int = paginas
        self.__isbn: str = isbn
        self.__categoria: Categoria = categoria
        self.__editora: Editora = editora
        self.__autor: Autor = autor

    @property
    def id(self) -> int:
        return self.__id
    
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def titulo(self) -> str:
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo: str):
        self.__titulo = titulo

    @property
    def resumo(self) -> str:
        return self.__resumo

    @resumo.setter
    def resumo(self, resumo: str):
        self.__resumo = resumo

    @property
    def ano(self) -> int:
        return self.__ano

    @ano.setter
    def ano(self, ano: int):
        self.__ano = ano

    @property
    def paginas(self) -> int:
        return self.__paginas

    @paginas.setter
    def paginas(self, paginas: int):
        self.__paginas = paginas

    @property
    def isbn(self) -> str:
        return self.__isbn

    @titulo.setter
    def isbn(self, isbn: str):
        self.__isbn = isbn

    @property
    def categoria(self) -> Categoria:
        return self.__categoria

    @categoria.setter
    def categoria(self, categoria: Categoria):
        self.__categoria = categoria

    @property
    def editora(self) -> Editora:
        return self.__editora

    @editora.setter
    def editora(self, editora: Editora):
        self.__editora = editora

    @property
    def autor(self) -> Autor:
        return self.__autor

    @autor.setter
    def autor(self, autor: Autor):
        self.__autor = autor