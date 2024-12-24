# biblioteca-virtual
Este projeto é uma aplicação de uma biblioteca virtual, desenvolvida em Python, que utiliza os conceitos de **Programação Orientada a Objetos (POO)**, uma interface gráfica criada com o **Tkinter** e um banco de dados utilizando o **Json**. A aplicação permite adicionar, listar, buscar, emprestar e devolver livros.

Este é um projeto de uma Biblioteca Virtual implementado em Python. O projeto consiste em três partes principais:
- **Classe `livro`**: Representa os livros na biblioteca, com informações como título, autor e status de empréstimo.
- **Classe `biblioteca`**: Gerencia uma coleção de livros, permitindo adicionar, listar, emprestar e devolver livros.
- **Classe `datarecord`**: Gerencia o banco de dados contendo em um arquivo .json, os livros salvos pela classe `biblioteca`.
- **Interface Gráfica (GUI)**: Uma aplicação gráfica feita com `tkinter` para interagir com a biblioteca de maneira visual.

## Estrutura do Projeto

### Arquivos
1. **`livro.py`**
   - Define a classe `livro`.
   - Cada instância da classe representa um livro com os atributos:
     - `titulo` (str): O título do livro.
     - `autor` (str): O autor do livro.
     - `emprestimo` (bool): Indica se o livro está emprestado.
   - Métodos principais:
     - `_emprestar()`: Marca o livro como emprestado.
     - `_devolver()`: Marca o livro como devolvido.
     - `__str__()`: Retorna uma descrição legível do livro, incluindo o título, autor e status.

2. **`biblioteca.py`**
   - Define a classe `biblioteca`.
   - Gerencia uma coleção de objetos da classe `livro`.
   - Métodos principais:
     - `add_livro(titulo, autor)`: Adiciona um novo livro à biblioteca.
     - `buscar_livro(titulo)`: Busca um livro pelo título.
     - `emprestar(titulo)`: Marca um livro como emprestado.
     - `devolver(titulo)`: Marca um livro como devolvido.

3. **`datajson.py`**
   - Define a classe `datarecord`.
   - Gerencia um banco de dados de objetos salvos pela classe `biblioteca`.
     - `save(model)`: Salva um objeto no arquivo `database_livro.json`.
     - `load()`: Carrega os objetos salvos no arquivo `database_livro.json`.
     - `remove(titulo)`: Remove um objeto no arquivo `database_livro.json`.
     - `alterar(titulo)`: Altera o atributo `emprestimo` em um objeto no arquivo `database_livro.json`.

4. **`main.py`**
   - Implementa a interface gráfica do projeto usando `tkinter`.
   - Permite ao usuário interagir com a biblioteca por meio de uma GUI estilizada.

### Funcionalidades
A aplicação permite:
1. **Adicionar Livros**: Insira o título e autor para adicionar um livro à biblioteca.
2. **Remover Livros**: Insira o título para remover um livro da biblioteca.
3. **Listar Livros**: Veja todos os livros disponíveis na biblioteca e seus status.
4. **Buscar Livros**: Pesquise um livro pelo título.
5. **Emprestar Livros**: Empreste um livro disponível.
6. **Devolver Livros**: Devolva um livro emprestado.

## Pré-requisitos
- Python 3.x instalado.
- O módulo padrão `tkinter` (incluso com o Python).
- O módulo padrão `json` (incluso com o Python).

## Como Executar
1. Certifique-se de que todos os arquivos (`livro.py`, `biblioteca.py`, `datajson.py` e `main.py`) estão em seus
   diretórios.
2. Execute o arquivo `main.py`:
   ```bash
   python3 main.py
3. Interaja com a interface gráfica para gerenciar a biblioteca.

## Exemplo de Uso
1. Abra a aplicação e insira o título e autor de um livro.
2. Clique em Adicionar Livro ou Remover Livro para adicioná-lo ou removê-lo da biblioteca.
3. Use os botões Listar Livros, Buscar Livro, Emprestar Livro e Devolver Livro para interagir com os livros.

## Estrutura do Código
   ```bash
   biblioteca_virtual/
   ├── package/
   │   ├── controllers/
   │   │   ├── db/
   │   │   │   ├── database_livro.json  # Arquivo .json
   │   │   ├── biblioteca.py            # Classe biblioteca
   │   │   ├── datajson.py              # Classe datarecord
   │   ├── model/
   │       ├── livro.py                 # Classe livro
   ├── icon.png                         # Arquivo .png para icone
   ├── main.py                          # Interface gráfica com Tkinter
   ├── README.md                        # Documentação do projeto
