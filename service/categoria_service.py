from dao.categoria_dao import CategoriaDAO
from model.categoria import Categoria

class CategoriaService:

    def __init__(self):
        self.__categoria_dao: CategoriaDAO = CategoriaDAO()

    @property
    def categoria_dao(self) -> CategoriaDAO:
        return self.__categoria_dao

    def menu(self):
        print('[Categorias] Escolha uma das seguintes opções:\n'
                '1 - Listar todas as categorias\n'
                '2 - Adicionar nova categoria\n'
                '3 - Excluir categoria\n'
                '4 - Ver categoria por Id\n'
                '0 - Voltar ao menu anterior\n')
        escolha = input('Digite a opção: ')

        if escolha == '0':
            return
        if escolha == '1':
            self.listar()
        elif escolha == '2':
            self.adicionar()
        elif escolha == '3':
            self.remover()
        elif escolha == '4':
            self.mostrar_por_id()
        else:
            print('Opção inválida! Por favor, tente novamente!')

        self.menu()

    def listar(self):
        print('\nListando categorias...')

        try:
            categorias = self.__categoria_dao.listar()
            if len(categorias) == 0:
                print('Nenhuma categoria encontrada!')

            for categoria in categorias:
                print(f'{categoria.id} | {categoria.nome}')
        except Exception as e:
            print(f'Erro ao exibir as categorias! - {e}')
            return

        input('Pressione uma tecla para continuar...')

    def adicionar(self):
        print('\nAdicionando categoria...')

        try:
            nome = input('Digite o nome da categoria: ')
            nova_categoria = Categoria(nome)
            self.__categoria_dao.adicionar(nova_categoria)
            print('Categoria adicionada com sucesso!')
        except Exception as e:
            print(f'Erro ao inserir categoria! - {e}')
            return

        input('Pressione uma tecla para continuar...')

    def remover(self):
        print('\nRemovendo categoria...')

        try:
            categoria_id = int(input('Digite o ID da categoria para excluir: '))
            if (self.__categoria_dao.remover(categoria_id)):
                print('Categoria excluída com sucesso!')
            else:
                print('Categoria não encontrada!')
        except Exception as e:
            print(f'Erro ao excluir categoria! - {e}')
            return
        
        input('Pressione uma tecla para continuar...')

    def mostrar_por_id(self):
        print('\nCategoria por Id...')

        try:
            id = int(input('Digite o Id da categoria para buscar: '))
            cat = self.__categoria_dao.buscar_por_id(id)

            if (cat == None):
                print('Categoria não encontrada!')
            else:
                print(f'Id: {cat.id} | Categoria: {cat.nome}')    
        except Exception as e:
            print(f'Erro ao exibir categoria! - {e}')
            return     
        
        input('Pressione uma tecla para continuar...')