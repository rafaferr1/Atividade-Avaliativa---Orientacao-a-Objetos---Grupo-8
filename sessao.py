class Sessao:
    def __init__(self, filme, sala, horario):
        self.filme = filme
        self.sala = sala
        self.horario = horario
        self.ingressos_vendidos = []
        # self.ingressos_disponiveis = ingressos_disponiveis

    def vender_ingresso(self, ingresso):
        if len(self.ingressos_vendidos) < self.sala.capacidade:
            self.ingressos_vendidos.append(ingresso)
            self.sala.ingressos_vendidos.append(ingresso)
            ingresso.disponivel = False
            return True
        else:
            return False