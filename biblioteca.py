from abc import ABC, abstractmethod

# Biblioteca
class Biblioteca:
    # Onde vai ficar armazenados os usuarios/livros
    usuarios = []
    livros_disponiveis = []
    livros_alugados = []
    # Exibição no geral
    def exibirUsuarios(self):
        for u in self.usuarios:
            livros_formatados = ", ".join(str(livro) for livro in u.get_lista()) if u.get_lista() else "Nenhum"
            print(f"Nome: {u.get_nome()} / E-mail: {u.get_email()} / {u.tipo()} / Livros: {livros_formatados}")

    def LivrosDisponiveis(self):
        for ld in self.livros_disponiveis:
            print(f"Titulo: {ld.get_titulo()} / Autor: {ld.get_autor()} / Ano: {ld.get_ano()} / Status: {ld.get_status()}")

    def LivrosAlugados(self):
        for livro, usuario in self.livros_alugados:
            print(f"Titulo: {livro.get_titulo()} / Autor: {livro.get_autor()} / Ano: {livro.get_ano()} / Status: {livro.get_status()} / Alugado por: {usuario.get_nome()}")

    # Cadastro
    def cadastrarUsuario(self):
        nome = input("Qual seu nome completo? ")
        email = input("Informe um e-mail para contato: ")
        while True:
            limite = input("Deseja ser usuário Regular ou VIP? (R/V) ")
            if limite.lower() == "r":
                usuario = UsuarioRegular(nome, email)
                break
            elif limite.lower() == "v":
                usuario = UsuarioVIP(nome, email)
                break    
            else:
                print("Opção inválida, digite R para regular ou V para VIP.")    

        self.usuarios.append(usuario)
        print(f"Usuário {usuario.get_nome()} {usuario.tipo()} cadastrado com sucesso!")

    # Cadastro do livro, fisdig quer dizer fisico/digital.
    def cadastrarLivro(self):
        titulo = input("Qual o titulo do livro? ")
        autor = input("Qual o autor do livro? ")
        ano = input("Qual o ano do livro? ")
        fisdig = input("O livro que deseja cadastrar é físico ou digital? (f/d) ")

        if fisdig.lower() == "d":
            livro = LivroDigital(titulo, autor, ano)
        else:
            livro = LivroFisico(titulo, autor, ano)

        self.livros_disponiveis.append(livro)
        print(f"Livro {titulo} cadastrado em nossa biblioteca com sucesso!")

    # Alugar um livro, checa se o usuário fez o cadastro, se não, volta pro menu. Também checa se o usuário passou dos limites de livro
    # fazendo essa comparação: len(usuario_encontrado.get_lista()) < usuario_encontrado.get_limite():#
    def alugarLivro(self):
        name_check = input("Qual seu nome completo? ")
        usuario_encontrado = None

        for usuario in self.usuarios:
            if usuario.get_nome().lower() == name_check.lower():
                usuario_encontrado = usuario
                break

        if usuario_encontrado:
            print("Usuário encontrado!")
        else:
            print("Usuário não está cadastrado, retornado ao menu...")
            return

        titulo = input("Qual o titulo do livro que deseja alugar? ")
        autor = input("Qual o autor do livro que deseja alugar? ")
        ano = input("De que ano é o livro que deseja alugar? ")
        status = input("Deseja a versão física ou digital? (f/d) ")

        if status.lower() == "d":
            livro = LivroDigital(titulo, autor, ano)
        else:
            livro = LivroFisico(titulo, autor, ano)

        if len(usuario_encontrado.get_lista()) < usuario_encontrado.get_limite():
            self.livros_alugados.append((livro, usuario_encontrado))
            lista_atual = usuario_encontrado.get_lista()
            lista_atual.append(livro)
            usuario_encontrado.set_lista(lista_atual)
            
            print(f"Livro {titulo} entregue ao usuário {usuario.get_nome()}")
            print(f"{livro.entregar()}")
        else:
            print("Você chegou ao limite de livros, devolva um de seus livros para conseguir alugar mais.")
            return
    # Mesma coisa que alugar, checa o usuário, mostra a lista de livros que ele tem e armazena a opção que escolher
    def devolverLivro(self):
        name_check = input("Qual seu nome completo? ")
        usuario_encontrado = None

        for usuario in self.usuarios:
            if usuario.get_nome().lower() == name_check.lower():
                usuario_encontrado = usuario
                break

        if usuario_encontrado:
            print("Usuário encontrado!")
        else:
            print("Usuário não está cadastrado, retornado ao menu...")
            return

        for livro in usuario_encontrado.get_lista():
            print(f"- {livro}")

        titulo = input("Qual o livro que deseja devolver? ")
        livro_para_devolver = None
        for livro in usuario_encontrado.get_lista():
            if livro.get_titulo().lower() == titulo.lower():
                livro_para_devolver = livro
                break

        if livro_para_devolver:
            lista_atual = usuario_encontrado.get_lista()
            lista_atual.remove(livro_para_devolver)
            usuario_encontrado.set_lista(lista_atual)
            self.livros_disponiveis.append(livro_para_devolver)

            for item in self.livros_alugados:
                if item[0] == livro_para_devolver and item[1] == usuario_encontrado:
                    self.livros_alugados.remove(item)
                    break

            print(f"Livro '{livro_para_devolver.get_titulo()}' devolvido com sucesso!")
        else:
            print("Livro não encontrado na sua lista.")
# Classes de usuário, livros e suas respectivas ''extensões''
class Usuario(ABC):
    def __init__(self, nome, email, limite):
        self._nome = nome
        self._email = email
        self._limite = limite
        self._lista = []

    def get_nome(self):
        return self._nome

    def get_email(self):
        return self._email

    def get_limite(self):
        return self._limite

    def get_lista(self):
        return self._lista

    @abstractmethod
    def tipo(self):
        pass

class UsuarioVIP(Usuario):
    def __init__(self, nome, email):
        super().__init__(nome, email, limite=6)
    def tipo(self):
        return "Usuário VIP"

class UsuarioRegular(Usuario):
    def __init__(self, nome, email):
        super().__init__(nome, email, limite=3)
    def tipo(self):
        return "Usuário Regular"

class Livro(ABC):
    def __init__(self, titulo, autor, ano, status):
        self._titulo = titulo
        self._autor = autor
        self._ano = ano
        self._status = status

    def get_titulo(self):
        return self._titulo

    def get_autor(self):
        return self._autor

    def get_ano(self):
        return self._ano

    def get_status(self):
        return self._status

    def __str__(self):
        return f"{self._titulo} ({self._ano}) - {self._autor} [{self._status}]"
    
    @abstractmethod
    def entregar(self):
        pass

class LivroFisico(Livro):
    def __init__(self, titulo, autor, ano):
        super().__init__(titulo, autor, ano, "Fisico")
    def entregar(self):
        print("Livro fisico entregue no balcão ao usuário.")

class LivroDigital(Livro):
    def __init__(self, titulo, autor, ano):
        super().__init__(titulo, autor, ano, "Digital")
        
    def entregar(self):
        print("Livro digital disponibilizado para o usuário.")
# Sobre a interface e os requisitos: O cadastro de usuário e livros foram feitos,
# gerenciamento de usuário eu separei pra ser apenas Exibir Usuários, a busca de livro seria as opções 6 e 7 tal como o relatório. 
# (Exibir Usuários mostra quem alugou, qual e se é fisico ou digital)
def Interface():
    biblioteca = Biblioteca()
    while True:
        print("---MENU---")
        print("1. Cadastrar Usuário")
        print("2. Cadastrar Livro")
        print("3. Alugar um Livro")
        print("4. Exibir Usuários")
        print("5. Devolver Livro")
        print("6. Livros Disponiveis")
        print("7. Livros Emprestados")

        escolha = input("Escolha uma das opções: ")
        if escolha == "1":
            biblioteca.cadastrarUsuario()
        elif escolha == "2":
            biblioteca.cadastrarLivro()
        elif escolha == "3":
            biblioteca.alugarLivro()
        elif escolha == "4":
            biblioteca.exibirUsuarios()
        elif escolha == "5":
            biblioteca.devolverLivro()
        elif escolha == "6":
            biblioteca.LivrosDisponiveis()
        elif escolha == "7":
            biblioteca.LivrosAlugados()
        else:
            print("Opção Inválida.")

Interface()