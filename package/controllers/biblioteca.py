from package.model.livro import livro

class biblioteca:
    livros_biblioteca = 0
    
    def __init__(self):
        self.itens = []

    def add_livro(self, titulo, autor):
        biblioteca.livros_biblioteca += 1
        novolivro = livro(titulo, autor)
        self.itens.append(novolivro)
        return f"Livro {titulo} foi adicionado à biblioteca!"

    def buscar_livro(self, busca):
        verificador = 0
        for livro in self.itens:
            if busca.lower() == livro.titulo.lower():
                return livro
                verificador = 1
        if verificador == 0:
            return False

    def emprestar(self, titulo):
        verificador = 0
        for livro in self.itens:
            if titulo.lower() == livro.titulo.lower():
                return livro._emprestar()
                verificador = 1
        if verificador == 0:
            return False

    def devolver(self, titulo):
        verificador = 0
        for livro in self.itens:
            if titulo.lower() == livro.titulo.lower():
                return livro._devolver()
                verificador = 1
        if verificador == 0:
            return False
