# Biblioteca
class Biblioteca:
    usuarios_cadastrados = []
    livros_disponiveis = []
    livros_emprestados = []

    def adicionarUsuario(self):
        nome = input("Qual o seu nome completo? ")
        email = input("E-mail para contato: ")
        lista_livros = []

        usuario = Usuario(nome, email, lista_livros)
        
        if any(u.email == email for u in self.usuarios_cadastrados):
            print("Usuário já cadastrado.")
        else:
            self.usuarios_cadastrados.append(usuario)
            print("Usuário Cadastrado com sucesso.")
    
    def exibirUsuarios(self):
        for u in self.usuarios_cadastrados:
            print(f"Nome: {u.nome} Email: {u.email} Livros: {u.lista_livros}")

    def exibirLivros(self):
        for l in self.livros_disponiveis:
            print(f"Livro: {l.titulo} Autor {l.autor} Ano {l.ano} Status {l.status}")

    def adicionarLivro(self):

        nome = input("Qual o seu nome completo? ")

        if any(u.nome.lower() == nome.lower() for u in self.usuarios_cadastrados):
            titulo = input("Qual o titulo do Livro? ")
            autor = input("Qual o autor do Livro? ")
            ano = input("Qual o ano do Livro? ")
            status = "Emprestado"

            print("Usuário encontrado, prossiga com o cadastro do livro.")

            novo_livro = Livro(titulo, autor, ano, status)

            self.livros_emprestados.append(novo_livro)
            print("Livro cadastrado com sucesso.")

        else:
            print("Usuário ainda não cadastrado.")

    def buscarLivro(self):

        buscalivro = input("Qual o livro que deseja procurar? ")

        if any(y.titulo.lower() == buscalivro.lower() for y in self.livros_disponiveis):
            print("Livro disponível, retorne ao menu para fazer o cadastro.")
        else:
            print("Livro indisponível.")

# Livro
class Livro:
    def __init__(self, titulo, autor, ano, status):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.status = status
# Usuário      
class Usuario:
    def __init__(self, nome, email, lista_livros):
        self.nome = nome
        self.email = email
        self.lista_livros = lista_livros

# Interface
def interface():

    biblioteca = Biblioteca()

    while True:
        print("Menu:")
        print("1. Cadastrar Usuário.")
        print("2. Cadastrar Livro.")
        print("3. Exibir Usuários")
        print("4. Exibir Livros Disponiveis")
        print("5. Buscar Livros")
        print("6. Sair")

        escolha = input("Escolha uma das opções: ")
        if escolha == "1":
            biblioteca.adicionarUsuario()
        elif escolha == "2":
            biblioteca.adicionarLivro()
        elif escolha == "3":
            biblioteca.exibirUsuarios()
        elif escolha == "4":
            biblioteca.exibirLivros()
        elif escolha == "5":
            biblioteca.buscarLivro()
        elif escolha == "6":
            break
        else:
            print("Escolha Inválida.")

interface()