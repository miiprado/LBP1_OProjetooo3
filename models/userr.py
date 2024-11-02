class Usuario:
    def __init__(self, id, nome, senha):
        self.id = id
        self.nome = nome
        self.senha = senha


listaUsuarios = []
listaUsuarios.append(Usuario(1, "Mirella", "123"))