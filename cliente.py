from pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome, cpf, idade, endereco, email, telefone):
        super().__init__(nome, cpf, idade, endereco)
        self.email = email
        self.telefone = telefone
        self.ingressos_comprados = []

    def comprar_ingresso(self, ingresso):
        self.ingressos_comprados.append(ingresso)
        print("Ingresso vendido para o cliente", self.nome)

    def mostrar_ingresso(self):
        return self.filme.titulo, self.filme.duracao, self.filme.genero, self.horario, self.preco