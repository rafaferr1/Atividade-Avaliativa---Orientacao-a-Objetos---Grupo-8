class Sala:
    def __init__(self, numero, capacidade):
        self.numero = numero
        self.capacidade = capacidade
        self.ingressos_vendidos = []
        self.clientes_registrados = []

    def vender_ingresso(self, ingresso):
        if len(self.ingressos_vendidos) < self.capacidade:
            self.ingressos_vendidos.append(ingresso)
            ingresso.disponivel = False
            return True
        else:
            return False


    def registrar_cliente(self, cliente):
        self.clientes_registrados.append(cliente)

    def ver_clientes_registrados(self):
        return self.clientes_registrados

    # def registrar_cliente(self, cliente):
    #   # Implementação do método
    #     for ingresso in cliente.ingressos_comprados:
    #         if ingresso in self.ingressos_vendidos:
    #             print(f"Cliente {self.nome} registrado com sucesso!")
    #             ingresso.cliente = cliente

    # def ver_clientes_registrados(self):
    #   # Implementação do método
    #     clientes_registrados = set()
    #     for ingresso in self.ingressos_vendidos:
    #         if ingresso.cliente:
    #             clientes_registrados.add(ingresso.cliente)
    #     return clientes_registrados