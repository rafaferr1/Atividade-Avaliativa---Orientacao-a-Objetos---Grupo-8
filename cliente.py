from pessoa import Pessoa

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