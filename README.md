"""
# Sistema de Gerenciamento de Biblioteca

## Descrição do projeto
Este projeto é um sistema desenvolvido em Python para controlar o acervo
de uma biblioteca. Ele permite cadastrar livros, realizar empréstimos,
devoluções, buscas, listagens e ordenação dos livros cadastrados.

Os dados dos livros são armazenados em uma lista de dicionários durante
a execução e salvos em um arquivo JSON para manter as informações mesmo
após o programa ser fechado.

---

## Como executar o programa

1. Ter o Python 3 instalado no computador.
2. Abrir o terminal na pasta do projeto.
3. Executar o comando:

python biblioteca.py

4. Utilizar o menu apresentado no terminal escolhendo as opções desejadas.

O arquivo livros.json será criado automaticamente para salvar os dados.

---

## Principais funcionalidades

- Cadastro de livros com:
  - Título
  - Autor
  - Ano de publicação
  - Código/ISBN
  - Status (disponível ou emprestado)

- Registro de empréstimos de livros.
- Registro de devoluções.
- Listagem de todos os livros cadastrados.
- Busca de livros por título ou autor.
- Ordenação dos livros por título, autor ou ano.
- Salvamento e carregamento dos dados em arquivo.

---

## Requisitos técnicos aplicados

- Menu principal utilizando if/elif/else:
  Aplicado no controle das opções do sistema.

- Estrutura de repetição while:
  Utilizada para manter o menu funcionando até a opção "sair".

- Funções próprias com parâmetros e retorno:
  Foram utilizadas funções como:
    - cadastrar_livro()
    - buscar_livro()
    - listar_livros()
    - emprestar_livro()
    - devolver_livro()
    - ordenar_livros()

- Lista de dicionários:
  Os livros são armazenados em uma lista, onde cada item é um dicionário
  contendo as informações do livro.

- Persistência de dados em arquivo:
  Utilização do arquivo livros.json para salvar e recuperar os dados.

- Biblioteca padrão do Python:
  Foi utilizada apenas a biblioteca json, sem instalação de pacotes externos.

