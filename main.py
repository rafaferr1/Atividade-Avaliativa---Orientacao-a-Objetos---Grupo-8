class Pessoa:
    def __init__(self, nome, cpf, idade, endereco):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.endereco = endereco

# from pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome, cpf, idade, endereco, email, telefone):
        super().__init__(nome, cpf, idade, endereco)
        self.email = email
        self.telefone = telefone
        self.ingressos_comprados = []

  
    def comprar_ingresso(self, ingresso):
        # Implementação do método
        self.ingressos_comprados.append(ingresso)
        print("Ingresso vendido para o cliente", Cliente.nome)


    def registrar_cliente(self):
        # Implementação do método
        print(f"Cliente {self.nome} registrado com sucesso!")

class Sessao:
    def __init__(self, filme, sala, horario):
        self.filme = filme
        self.sala = sala
        self.horario = horario
        self.ingressos_vendidos = []

    def vender_ingresso(self, ingresso):
        if len(self.ingressos_vendidos) < self.sala.capacidade:
            self.ingressos_vendidos.append(ingresso)
            self.sala.ingressos_vendidos.append(ingresso)
            ingresso.disponivel = False
            return True
        else:
            return False

class Ingresso:
    def __init__(self, filme, horario, preco):
        self.filme = filme
        self.horario = horario
        self.preco = preco
        self.disponivel = True

class Filme:
    def __init__(self, titulo, duracao, genero):
        self.titulo = titulo
        self.duracao = duracao
        self.genero = genero


class Sala:
    def __init__(self, numero, capacidade):
        self.numero = numero
        self.capacidade = capacidade
        self.ingressos_vendidos = []

    def vender_ingresso(self, ingresso):
        if len(self.ingressos_vendidos) < self.capacidade:
            self.ingressos_vendidos.append(ingresso)
            ingresso.disponivel = False
            return True
        else:
            return False






          #DA UMA OLHADA AQUI PESSOAL#
#cliente1.comprar_ingresso(ingresso1)
#sala1.vender_ingresso(ingresso1)

#from sala import Sala
#from ingresso import Ingresso
#from filme import Filme
#from pessoa import Pessoa
#from cliente import Cliente
#from sessao import Sessao

#cliente = Cliente("email", 5555, 55555, 55555, 55555 ,5555)
#sala = Sala(11, 1)
#filme = Filme(111, 22, 444)
#ingresso = Ingresso(filme, 22, 33)
#ingresso = Ingresso(filme, 22, 33)
#essao = Sessao(filme, 11, 11)