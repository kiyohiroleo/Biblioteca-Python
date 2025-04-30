# Biblioteca
class Biblioteca:
    usuarios_cadastrados = []
    livros_disponiveis = []
    livros_emprestados = []

    def adicionarUsuario(self):
        nome = input("Qual o seu nome completo? ")
        email = input("E-mail para contato: ")
        limite_livros = input("Gostaria de ser um membro VIP? (S/N) ")
        if limite_livros.lower() == "s":
            usuario = UsuarioVIP(nome, email)
        else:
            usuario = UsuarioRegular(nome, email)
        
        if any(u.email == email for u in self.usuarios_cadastrados):
            print("Usuário já cadastrado.")
        else:
            self.usuarios_cadastrados.append(usuario)
            print("Usuário Cadastrado com sucesso.")
    
    def exibirUsuarios(self):
        for u in self.usuarios_cadastrados:
            if u.membro == 6:
                print(f"Nome: {u.nome} | Email: {u.email} Livros: {u.lista_de_livros} Membro: {"VIP", u.membro, "de limite."}")
            else:
                print(f"Nome: {u.nome} | Email: {u.email} Livros: {u.lista_de_livros} Membro: {"Regular", u.membro, "de limite"}")


    def exibirLivrosEmprestados(self):
        for l in self.livros_emprestados:
            print(f"Livro: {l.titulo} | Autor {l.autor} | Ano {l.ano} | Status {l.status}")

    def exibirLivrosDisponiveis(self):
        for l in self.livros_disponiveis:
            print(f"Livro: {l.titulo} | Autor {l.autor} | Ano {l.ano} | Status {l.status}")

    def adicionarLivro(self):

        nome = input("Qual o seu nome completo? ")

        if any(u.nome.lower() == nome.lower() for u in self.usuarios_cadastrados):
            titulo = input("Qual o titulo do Livro? ")
            autor = input("Qual o autor do Livro? ")
            ano = input("Qual o ano do Livro? ")
            status = input("Gostaria de uma versão física ou digital do Livro? ")
            
            livro = Livro(titulo, autor, ano, status)
            self.livros_emprestados.append(livro)

            if status.lower() == "digital":
                status = LivroDigital(titulo, autor, ano, status)
            else:
                status = LivroFisico(titulo, autor, ano, status)

            print("Usuário encontrado, prossiga com o cadastro do livro.")

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

class LivroFisico(Livro):
    def __init__(self, titulo, autor, ano, status):
        super().__init__(titulo, autor, ano, status)

class LivroDigital(Livro):
    def __init__(self, titulo, autor, ano, status):
        super().__init__(titulo, autor, ano, status)

# Usuário      
class Usuario:
    def __init__(self, nome, email, membro):
        self.nome = nome
        self.email = email
        self.membro = membro
        self.lista_de_livros = []

class UsuarioRegular(Usuario):
    def __init__(self, nome, email):
        super().__init__(nome, email, membro = 3)

class UsuarioVIP(Usuario):
    def __init__(self, nome, email):
        super().__init__(nome, email, membro = 6)

# Interface
def interface():

    biblioteca = Biblioteca()

    while True:
        print("Menu:")
        print("1. Cadastrar Usuário.")
        print("2. Cadastrar Livro.")
        print("3. Exibir Usuários")
        print("4. Exibir Livros Disponiveis")
        print("5. Exibir Livros Disponiveis")
        print("6. Buscar Livros")
        print("7. Sair")

        escolha = input("Escolha uma das opções: ")
        if escolha == "1":
            biblioteca.adicionarUsuario()
        elif escolha == "2":
            biblioteca.adicionarLivro()
        elif escolha == "3":
            biblioteca.exibirUsuarios()
        elif escolha == "4":
            biblioteca.exibirLivrosEmprestados()
        elif escolha == "5":
            biblioteca.exibirLivrosDisponiveis()
        elif escolha == "6":
            biblioteca.buscarLivro()
        elif escolha == "7":
            break
        else:
            print("Escolha Inválida.")

interface()