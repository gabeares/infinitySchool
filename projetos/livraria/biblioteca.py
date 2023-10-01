from livros.livroFisico import LivroFisico
# from livros.livroDigital import LivroDigital
from membros.membro import Membro


class Biblioteca:
    def __init__(self):
        self.__livros = []
        self.__membros = []

    def cadastrarMembro(self, membro: Membro):
        self.__membros.append(membro)
        print('Novo membro adicionado')

    def deletarMembro(self, id):
        for membro in self.__membros:
            if membro.id == id:
                self.__membros.remove(membro)
                print('Membro deletado com sucesso')

    def cadastrarLivro(self, livro: LivroFisico):
        self.__livros.append(livro)
        print('Novo livros adicionado')

    def deletarLivro(self, id):
        for livro in self.__livros:
            if livro.id == id:
                self.__livros.remove(livro)
                print('Livro deletado com sucesso')

    def listarLivros(self):
        print('----- Livros Cadastrados -----')
        for livro in self.__livros:
            print(f'----- Dados -----')
            print(f'Id: {livro.id}')
            print(f'Nome: {livro.nome}')
            print(f'Autor: {livro.autor}')
            print(f'Ano: {livro.ano}')
            print(f'Págs: {livro.pags}')

    def listarMembros(self):
        pass