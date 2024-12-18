from package_biblioteca import biblioteca
from tkinter import messagebox
import tkinter as tk

# instancia classe biblioteca
biblioteca_int = biblioteca()

# funcoes para os botoes
def adicionar_livro():
    titulo = entrada_titulo.get()
    autor = entrada_autor.get()

    if titulo and autor:
        messagebox.showinfo("Sucesso", message=biblioteca_int.add_livro(titulo, autor))
        entrada_titulo.delete(0, tk.END)
        entrada_autor.delete(0, tk.END)
    else:
        messagebox.showwarning("Erro", message="Por favor, preencha o título e o autor.")

def listar_livro():
    contagem = f"total de livros disponiveis: {biblioteca_int.livros_biblioteca}"
    itens = biblioteca_int.itens

    if itens:
        lista = "\n".join([str(contagem)])
        lista = "\n".join([str(livro) for livro in itens])
        messagebox.showinfo("Livros na Biblioteca", message=lista)
    else:
        messagebox.showinfo("Livros na Biblioteca", message="Nenhum livro disponível na biblioteca.")

def buscar_livro():
    busca = entrada_busca.get()

    if busca:
        text = biblioteca_int.buscar_livro(busca)
        if text == False:
            messagebox.showinfo("Erro", message=f"Livro {busca} não encontrado.")
        else:
            messagebox.showinfo("Resultado", message=text)
    else:
        messagebox.showwarning("Erro", message="Por favor, insira o título do livro.")

def emprestar_livro():
    titulo = entrada_acao.get()
    if titulo:
        text = biblioteca_int.emprestar(titulo)
        if text == False:
            messagebox.showinfo("Erro", message=f"Livro {titulo} não encontrado.")
        else:
            messagebox.showinfo("Resultado", message=text)
    else:
        messagebox.showwarning("Erro", message="Por favor, insira o título do livro.")

def devolver_livro():
    titulo = entrada_acao.get()
    if titulo:
        text = biblioteca_int.devolver(titulo)
        if text == False:
            messagebox.showinfo("Erro", message=f"Livro {titulo} não encontrado.")
        else:
            messagebox.showinfo("Resultado", message=text)
    else:
        messagebox.showwarning("Erro", message="Por favor, insira o título do livro.")

# configuracao da interface
root = tk.Tk()
root.title("Biblioteca Virtual")
root.geometry("500x300")
root.configure(bg="#ECE9D8")

root.option_add("*Font", "Tahoma 10")
root.option_add("*Button.Background", "#F0F0F0")
root.option_add("*Button.Foreground", "black")
root.option_add("*Label.Background", "#ECE9D8")
root.option_add("*Label.Foreground", "black")
root.option_add("*Entry.Background", "white")

# layout principal
frame_principal = tk.Frame(root, bg="#ECE9D8", padx=10, pady=10)
frame_principal.pack()

# campo para adicionar livros
tk.Label(frame_principal, text="Título:").grid(row=0, column=0, sticky="w")
entrada_titulo = tk.Entry(frame_principal, width=30)
entrada_titulo.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_principal, text="Autor:").grid(row=1, column=0, sticky="w")
entrada_autor = tk.Entry(frame_principal, width=30)
entrada_autor.grid(row=1, column=1, padx=5, pady=5)

# botao para adicionar livros
add = tk.Button(frame_principal, text="Adicionar Livro", command=adicionar_livro)
add.grid(row=2, column=1, pady=10)

# campo para buscar livros
tk.Label(frame_principal, text="Busca:").grid(row=3, column=0, sticky="w")
entrada_busca = tk.Entry(frame_principal, width=30)
entrada_busca.grid(row=3, column=1, padx=5, pady=5)

# botao para listar livros
listar = tk.Button(frame_principal, text="Listar Livros", command=listar_livro)
listar.grid(row=4, column=0, pady=10)

# botao para buscar livros
busca = tk.Button(frame_principal, text="Buscar Livro", command=buscar_livro)
busca.grid(row=4, column=1, pady=10)

# campo para emprestar ou devolver livros
tk.Label(frame_principal, text="Título para ação:").grid(row=5, column=0, sticky="w")
entrada_acao = tk.Entry(frame_principal, width=30)
entrada_acao.grid(row=5, column=1, padx=5, pady=5)

emprestar = tk.Button(frame_principal, text="Emprestar Livro", command=emprestar_livro)
emprestar.grid(row=6, column=0, pady=10)
devolver = tk.Button(frame_principal, text="Devolver Livro", command=devolver_livro)
devolver.grid(row=6, column=1, pady=10)

# executar a interface
root.mainloop()
