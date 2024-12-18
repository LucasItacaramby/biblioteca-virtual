# biblioteca-virtual
Este projeto é uma aplicação de uma biblioteca virtual, desenvolvida em Python, que utiliza os conceitos de **Programação Orientada a Objetos (POO)** e uma interface gráfica criada com o **Tkinter**. A aplicação permite adicionar, listar, buscar, emprestar e devolver livros.

Este é um projeto de uma Biblioteca Virtual implementado em Python. O projeto consiste em três partes principais:
- **Classe `livro`**: Representa os livros na biblioteca, com informações como título, autor e status de empréstimo.
- **Classe `biblioteca`**: Gerencia uma coleção de livros, permitindo adicionar, listar, emprestar e devolver livros.
- **Interface Gráfica (GUI)**: Uma aplicação gráfica feita com `tkinter` para interagir com a biblioteca de maneira visual.

## Estrutura do Projeto

### Arquivos
1. **`package_livro.py`**
   - Define a classe `livro`.
   - Cada instância da classe representa um livro com os atributos:
     - `titulo` (str): O título do livro.
     - `autor` (str): O autor do livro.
     - `emprestimo` (bool): Indica se o livro está emprestado.
   - Métodos principais:
     - `_emprestar()`: Marca o livro como emprestado.
     - `_devolver()`: Marca o livro como devolvido.
     - `__str__()`: Retorna uma descrição legível do livro, incluindo o título, autor e status.

2. **`package_biblioteca.py`**
   - Define a classe `biblioteca`.
   - Gerencia uma coleção de objetos da classe `livro`.
   - Métodos principais:
     - `add_livro(titulo, autor)`: Adiciona um novo livro à biblioteca.
     - `buscar_livro(titulo)`: Busca um livro pelo título.
     - `emprestar(titulo)`: Marca um livro como emprestado.
     - `devolver(titulo)`: Marca um livro como devolvido.

3. **`interface.py`**
   - Implementa a interface gráfica do projeto usando `tkinter`.
   - Permite ao usuário interagir com a biblioteca por meio de uma GUI estilizada.

### Funcionalidades
A aplicação permite:
1. **Adicionar Livros**: Insira o título e autor para adicionar um livro à biblioteca.
2. **Listar Livros**: Veja todos os livros disponíveis na biblioteca e seus status.
3. **Buscar Livros**: Pesquise um livro pelo título.
4. **Emprestar Livros**: Empreste um livro disponível.
5. **Devolver Livros**: Devolva um livro emprestado.

## Pré-requisitos
- Python 3.x instalado.
- O módulo padrão `tkinter` (incluso com o Python).

## Como Executar
1. Certifique-se de que todos os arquivos (`package_livro.py`, `package_biblioteca.py` e `interface.py`) estão no mesmo diretório.
2. Execute o arquivo `interface.py`:
   ```bash
   python3 interface.py
3. Interaja com a interface gráfica para gerenciar a biblioteca.

## Exemplo de Uso
1. Abra a aplicação e insira o título e autor de um livro.
2. Clique em Adicionar Livro para adicioná-lo à biblioteca.
3. Use os botões Listar Livros, Buscar Livro, Emprestar Livro e Devolver Livro para interagir com os livros.

## Estrutura do Código
   ```bash
   biblioteca_virtual/
   ├── package_livro.py        # Classe livro
   ├── package_biblioteca.py   # Classe biblioteca
   ├── interface.py            # Interface gráfica com Tkinter
   ├── README.md               # Documentação do projeto
