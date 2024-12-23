from package.model.livro import livro
from package.controllers.datajson import datarecord

class biblioteca:
    def __init__(self):
        self.database = datarecord()
        self.itens = self.database.load()

    def add_livro(self, titulo, autor):
        for i in self.itens:
            if titulo.lower() == i.titulo.lower():
                return False
        novolivro = livro(titulo, autor, False)

        self.itens.append(novolivro)
        self.database.save(novolivro)

        return f"Livro {titulo} foi adicionado à biblioteca!"
    
    def rm_livro(self, titulo):
        verificador = 0
        for i in self.itens:
            if titulo.lower() == i.titulo.lower():
                verificador = 1
                self.database.remove(i.titulo)
                self.itens.remove(i)

                return f"Livro {titulo} foi removido da biblioteca!"
        if verificador == 0:
            return False

    def buscar_livro(self, busca):
        verificador = 0
        for livro in self.itens:
            if busca.lower() == livro.titulo.lower():
                verificador = 1
                return livro
        if verificador == 0:
            return False

    def emprestar(self, titulo):
        verificador = 0
        for livro in self.itens:
            if titulo.lower() == livro.titulo.lower():
                verificador = 1
                info = livro._emprestar()
                if info == f"Você pegou o livro {livro.titulo}!":
                    self.database.alterar(titulo)
                return info
        if verificador == 0:
            return False

    def devolver(self, titulo):
        verificador = 0
        for livro in self.itens:
            if titulo.lower() == livro.titulo.lower():
                verificador = 1
                info = livro._devolver()
                if info == f"Você devolveu o livro {livro.titulo}!":
                    self.database.alterar(titulo)
                return info
        if verificador == 0:
            return False
