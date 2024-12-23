from package.model.livro import livro
import json

class datarecord:
    def __init__(self):
        self.filename = "package/controllers/db/database_livro.json"
        self.models = []

    def save(self, model):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
        
            if "livros" in data:
                data["livros"].append(vars(model))
            else:
                data["livros"] = [vars(model)]
        
            with open(self.filename, "w") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
        except FileNotFoundError:
            print(f"O arquivo {self.filename} não foi encontrado.")
        except Exception as e:
            print(f"Erro ao adicionar o livro: {e}")

    def load(self):
        try:
            with open(self.filename, "r") as file:
                data_dict = json.load(file)

            data = list(data_dict["livros"])
            for i in data:
                novolivro = livro(i['titulo'], i['autor'], i['emprestimo'])
                self.models.append(novolivro)
            return self.models
        except FileNotFoundError:
            print(f"O arquivo {self.__filename} não existe!")

    def remove(self, titulo):
        try:
            with open(self.filename, "r") as file:
                data_dict = json.load(file)
                
            data = list(data_dict["livros"])
            for i, livro in enumerate(data):
                if (livro['titulo'] == titulo):
                    del data_dict["livros"][i]
            
            with open(self.filename, "w") as remove:
                json.dump(data_dict, remove, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Erro ao remover os dados: {e}")

    def alterar(self, titulo):
        try:
            with open(self.filename, "r") as file:
                data_dict = json.load(file)
                
            data = list(data_dict["livros"])
            for i, livro in enumerate(data):
                if (livro['titulo'] == titulo):
                    if (livro['emprestimo'] == False):
                        livro['emprestimo'] = True
                    else:
                        livro['emprestimo'] = False
            
            with open(self.filename, "w") as remove:
                json.dump(data_dict, remove, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Erro ao alterar o modelo: {e}")
