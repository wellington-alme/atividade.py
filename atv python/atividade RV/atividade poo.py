from abc import ABC, abstractmethod
#Wellington Dos Santos Almeida

class Pessoa(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    @abstractmethod
    def obter_tipo_usuario(self):
        pass


class UsuarioComum(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula
        self.livros_emprestados = []

    def obter_tipo_usuario(self):
        return "Comum"

    def emprestar_livro(self, livro):
        if len(self.livros_emprestados) < 3 and livro.status == "Disponível":
            self.livros_emprestados.append(livro)
            livro.status = "Emprestado"
            return True
        return False

    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:
            self.livros_emprestados.remove(livro)
            livro.status = "Disponível"
            return True
        return False


class Administrador(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def obter_tipo_usuario(self):
        return "Administrador"

    def cadastrar_usuario(self, usuarios, usuario):
        usuarios.append(usuario)
    
    def cadastrar_livro(self, biblioteca, livro):
        biblioteca.append(livro)


class ItemBiblioteca(ABC):
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.status = "Disponível"  
    
    @abstractmethod
    def exibir_info(self):
        pass


class Livro(ItemBiblioteca):
    def __init__(self, titulo, autor, ano_publicacao):
        super().__init__(titulo, autor, ano_publicacao)

    def exibir_info(self):
        return f"Livro: {self.titulo}, Autor: {self.autor}, Ano: {self.ano_publicacao}, Status: {self.status}"


def relatorio_livros_disponiveis(biblioteca):
    for livro in biblioteca:
        if livro.status == "Disponível":
            print(livro.exibir_info())

def relatorio_usuarios_com_livros_emprestados(usuarios):
    for usuario in usuarios:
        if len(usuario.livros_emprestados) > 0:
            print(f"Usuário: {usuario.nome}, Livros Emprestados: {[livro.titulo for livro in usuario.livros_emprestados]}")


if __name__ == "__main__":
    
    admin = Administrador("Ana", 30, "A123")
    usuario1 = UsuarioComum("Carlos", 25, "U001")
    usuario2 = UsuarioComum("Beatriz", 28, "U002")

    livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)
    livro2 = Livro("Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997)

    biblioteca = [livro1, livro2]
    usuarios = []

    
    admin.cadastrar_usuario(usuarios, usuario1)
    admin.cadastrar_usuario(usuarios, usuario2)
    admin.cadastrar_livro(biblioteca, livro1)
    admin.cadastrar_livro(biblioteca, livro2)


    usuario1.emprestar_livro(livro1)
    
    
    print("Relatório de Livros Disponíveis:")
    relatorio_livros_disponiveis(biblioteca)
    
    print("\nRelatório de Usuários com Livros Emprestados:")
    relatorio_usuarios_com_livros_emprestados(usuarios)
