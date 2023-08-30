from model.livro import Livro

class LivroDAO:

    def __init__(self):
        self.__livros: list[Livro] = list()

    def listar(self) -> list[Livro]:
        return self.__livros

    def adicionar(self, livro: Livro) -> None:
        self.__livros.append(livro)

    def remover(self, livro_id: int) -> bool:
        encontrado = False
        for l in self.__livros:
            if (l.id == livro_id):
                index = self.__livros.index(l)
                self.__livros.pop(index)
                encontrado = True
                break
        return encontrado

    def buscar_por_id(self, livro_id) -> Livro:
        liv = None
        for l in self.__livros:
            if (l.id == livro_id):
                liv = l
                break
        return liv
    
    def ultimo_id(self) -> int:
        index = len(self.__livros) -1
        if (index == -1):
            id = 0
        else:
            id = self.__livros[index].id
        return id
    