class Pessoa:
    def __init__(self, nome, cpf, idade, endereco):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.endereco = endereco

class Cliente(Pessoa):
    def __init__(self, nome, cpf, idade, endereco, email, telefone):
        super().__init__(nome, cpf, idade, endereco)
        self.email = email
        self.telefone = telefone
        self.ingressos_comprados = []

    def comprar_ingresso(self, sessao, quantidade):
        if sessao.ingressos_disponiveis >= quantidade:
            ingresso = Ingresso(sessao, self, quantidade)
            self.ingressos_comprados.append(ingresso)
            sessao.ingressos_disponiveis -= quantidade
            return ingresso
        else:
            return None

class Sessao:
    def __init__(self, filme, sala, horario, ingressos_disponiveis):
        self.filme = filme
        self.sala = sala
        self.horario = horario
        self.ingressos_disponiveis = ingressos_disponiveis

class Ingresso:
    def __init__(self, sessao, cliente, quantidade):
        self.sessao = sessao
        self.cliente = cliente
        self.quantidade = quantidade

class Filme:
    def __init__(self, titulo, duracao, genero):
        self.titulo = titulo
        self.duracao = duracao
        self.genero = genero

class Sala:
    def __init__(self, numero, capacidade):
        self.numero = numero
        self.capacidade = capacidade