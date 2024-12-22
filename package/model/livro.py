class livro:
	def __init__(self, titulo, autor, emprestimo):
		self.titulo = titulo
		self.autor = autor
		self.emprestimo = emprestimo

	def _emprestar(self):
		if self.emprestimo == True:
			return f"Livro {self.titulo} não disponivel."
		elif self.emprestimo == False:
			self.emprestimo = True
			return f"Você pegou o livro {self.titulo}!"

	def _devolver(self):
		if self.emprestimo == False:
			return f"Livro {self.titulo} não foi emprestado."
		elif self.emprestimo == True:
			self.emprestimo = False
			return f"Você devolveu o livro {self.titulo}!"
		
	def __str__(self):
		status = "emprestado" if self.emprestimo else "disponível"
		return f"- livro: {self.titulo} de {self.autor}, status: {status}"
