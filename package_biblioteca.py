from package_livro import livro

class biblioteca:
    livros_biblioteca = 0
    
    def __init__(self):
        self.itens = []

    def add_livro(self, titulo, autor):
        biblioteca.livros_biblioteca += 1
        novolivro = livro(titulo, autor)
        self.itens.append(novolivro)
        print(f"Livro {titulo} foi adicionado à biblioteca")

    def listar_livros(self):
        print(f"total de livros disponiveis: {biblioteca.livros_biblioteca}")
        if self.itens:
            for livro in self.itens:
                print(f"- livro: {livro.titulo}, autor: {livro.autor}")
        else:
            print("a biblioteca está vazia")

    def buscar_livro(self, busca):
        verificador = 0
        for livro in self.itens:
            if busca.lower() == livro.titulo.lower():
                print(livro)
                verificador = 1
        if verificador == 0:
            print(f"Livro {busca} não encontrado!")

    def emprestar(self, titulo):
        verificador = 0
        for livro in self.itens:
            if titulo.lower() == livro.titulo.lower():
                print(livro._emprestar())
                verificador = 1
        if verificador == 0:
            print(f"Livro {titulo} não encontrado!")

    def devolver(self, titulo):
        verificador = 0
        for livro in self.itens:
            if titulo.lower() == livro.titulo.lower():
                print(livro._devolver())
                verificador = 1
        if verificador == 0:
            print(f"Livro {titulo} não encontrado!")
