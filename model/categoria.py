class Categoria:

    def __init__(self, nome: str, id=0):
        self.__id = id
        self.__nome: str = nome

    @property
    def id(self) -> int:
        return f'{self.__id}'

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @staticmethod
    def depositar():
        return "Opa"