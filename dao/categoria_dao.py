from model.categoria import Categoria
from typing import List


class CategoriaDAO:

    def __init__(self):
        self.__categorias: List[Categoria] = list()

    def listar(self) -> List[Categoria]:
        return self.__categorias

    def adicionar(self, categoria: Categoria) -> None:
        self.__categorias.append(categoria)

    def remover(self, categoria_id: int) -> bool:
        encontrado = False
        
        for c in self.__categorias:
            if (c.id == categoria_id):
                index = self.__categorias.index(c)
                self.__categorias.pop(index)
                encontrado = True
                break
        return encontrado

    def buscar_por_id(self, categoria_id) -> Categoria:
        cat = None
        for c in self.__categorias:
            if (c.id == categoria_id):
                cat = c
                break
        return cat
    
    def ultimo_id(self) -> int:
        index = len(self.__categorias) -1
        if (index == -1):
            id = 0
        else:
            id = self.__categorias[index].id
        return id
    