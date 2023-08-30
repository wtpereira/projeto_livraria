from model.autor import Autor

class AutorDAO:

    def __init__(self):
        self.__autores: list[Autor] = list()

    def listar(self) -> list[Autor]:
        return self.__autores

    def adicionar(self, autor: Autor) -> None:
        self.__autores.append(autor)

    def remover(self, autor_id: int) -> bool:
        encontrado = False
        for a in self.__autores:
            if (a.id == autor_id):
                index = self.__autores.index(a)
                self.__autores.pop(index)
                encontrado = True
                break
        return encontrado

    def buscar_por_id(self, autor_id) -> Autor:
        aut = None
        for a in self.__autores:
            if (a.id == autor_id):
                aut = a
                break
        return aut
    
    def ultimo_id(self) -> int:
        index = len(self.__autores) -1
        if (index == -1):
            id = 0
        else:
            id = self.__autores[index].id
        return id
    