from abc import ABC, abstractmethod

# Biblioteca
class Biblioteca:
    usuarios = []
    livros_disponiveis = []
    livros_alugados = []
# Exibir Usuários
    def exibirUsuarios(self):
        for u in self.usuarios:
            livros_formatados = ", ".join(str(livro) for livro in u.lista) if u.lista else "Nenhum"
            print(f"Nome: {u.nome} / E-mail: {u.email} / {'VIP' if u.limite > 3 else 'Regular'} / Livros: {livros_formatados}")
# Exibir Livros Disponiveis
    def LivrosDisponiveis(self):
        for ld in self.livros_disponiveis:
            print(f"Titulo: {ld.titulo} / Autor: {ld.autor} / Ano: {ld.ano} / Status: {ld.status}")
    def LivrosAlugados(self):
        for livro, usuario in self.livros_alugados:
            print(f"Titulo: {livro.titulo} / Autor: {livro.autor} / Ano: {livro.ano} / Status: {livro.status} / Alugado por: {usuario.nome}")

# Cadastrar Usuarios
    def cadastrarUsuario(self):
        nome = input("Qual seu nome completo? ")
        email = input("Informe um e-mail para contato: ")
        limite = input("Deseja ser um usuário Regular ou VIP? (R/V) ")

        if limite.lower() == "v":
            usuario = UsuarioVIP(nome, email)
        else:
            usuario = UsuarioRegular(nome, email)
        
        self.usuarios.append(usuario)
        print(f"Usuário {nome} cadastrado com sucesso!")
# Cadastrar Livros.
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
# Alugar Livros.
    def alugarLivro(self):
        name_check = input("Qual seu nome completo? ")
        usuario_encontrado = None
        
        for usuario in self.usuarios:
            if usuario.nome.lower() == name_check.lower():
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
        
        if len(usuario_encontrado.lista) < usuario_encontrado.limite:
            self.livros_alugados.append((livro, usuario_encontrado))
            usuario_encontrado.lista.append(livro)
            print("Livro adicionado com sucesso!")
            print(f"Livro {titulo} alugado com sucesso em nome de {name_check}!")
        else:
            print("Você chegou ao limite de livros, atualize para VIP para conseguir alugar mais.")
            return
# Devolução de Livros.
    def devolverLivro(self):
        name_check = input("Qual seu nome completo? ")
        usuario_encontrado = None
        
        for usuario in self.usuarios:
            if usuario.nome.lower() == name_check.lower():
                usuario_encontrado = usuario
                break
        
        if usuario_encontrado:
            print("Usuário encontrado!")
        else:
            print("Usuário não está cadastrado, retornado ao menu...")
            return
        
        for livro in usuario_encontrado.lista:
            print(f"- {livro}")

        titulo = input("Qual o livro que deseja devolver? ")
        livro_para_devolver = None
        for livro in usuario_encontrado.lista:
            if livro.titulo.lower() == titulo.lower():
                livro_para_devolver = livro
                break

        if livro_para_devolver:
            usuario_encontrado.lista.remove(livro_para_devolver)
            self.livros_disponiveis.append(livro_para_devolver)

            for item in self.livros_alugados:
                if item[0] == livro_para_devolver and item[1] == usuario_encontrado:
                    self.livros_alugados.remove(item)
                    break

            print(f"Livro '{livro_para_devolver.titulo}' devolvido com sucesso!")
        else:
            print("Livro não encontrado na sua lista.")

#Usuario e suas subclasses Regular e VIP
class Usuario:
    def __init__(self, nome, email, limite):
        self._nome = nome
        self._email = email
        self._limite = limite
        self._lista = []

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    def get_limite(self):
        return self._limite

    def set_limite(self, limite):
        if limite >= 3:
            self._limite = limite
        else:
            print("limite não pode ser menor que 3")

    def get_lista(self):
        return self._lista

    def set_lista(self, lista):
        self._lista = lista


class UsuarioVIP(Usuario):
    def __init__(self, nome, email):
        super().__init__(nome, email, limite=6)


class UsuarioRegular(Usuario):
    def __init__(self, nome, email):
        super().__init__(nome, email, limite=3)


class Livro:
    def __init__(self, titulo, autor, ano, status):
        self._titulo = titulo
        self._autor = autor
        self._ano = ano
        self._status = status

    def get_titulo(self):
        return self._titulo

    def set_titulo(self, titulo):
        self._titulo = titulo

    def get_autor(self):
        return self._autor

    def set_autor(self, autor):
        self._autor = autor

    def get_ano(self):
        return self._ano

    def set_ano(self, ano):
        self._ano = ano

    def get_status(self):
        return self._status

    def set_status(self, status):
        self._status = status

    def __str__(self):
        return f"{self._titulo} ({self._ano}) - {self._autor} [{self._status}]"


class LivroFisico(Livro):
    def __init__(self, titulo, autor, ano):
        super().__init__(titulo, autor, ano, "Fisico")


class LivroDigital(Livro):
    def __init__(self, titulo, autor, ano):
        super().__init__(titulo, autor, ano, "Digital")


# Interface
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

Interface()