import json

class datarecord:
    def __init__(self):
        self.filename = "package/controllers/db/database_livro.json"
        self.models = []

    def save(self):
        try:
            with open(self.filename, "w") as file:
                json.dump(self.models, file, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Erro ao salvar os dados: {e}")

    def record(self, model):
        try:
            self.models.append(vars(model))
            self.save()
        except Exception as e:
            print(f"Erro ao adicionar o modelo: {e}")

    def load(self):
        try:
            with open(self.filename, "r") as file:
                self.models = json.load(file)
                return self.models
        except FileNotFoundError as e:
            print(f"O arquivo {self.__filename} não existe!")
