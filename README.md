# Atividade Avaliativa:

Grupo: MatheusProtti, Thiago Adam, Gabriel Garcia e Rafael Ferreira

PARTE 1: - Configure o GitHub no VSCode. Todo o processo de codificacao deve ser feito utilizando o vscode com github e cada um dos integrantes deve fazer uma parte do trabalho utilizando o git. 

PARTE 2: Faça o diagrama de classes no draw.io, plnatuml ou outro de sua escolha. Implemente as classes com os relacionamentos e as heranças necessarias para um sistema de compra de ingressos de Cinema em Python. Implemente os metodos de acordo com a regra de negocios, como por exemplo, registrar clientes e/ou Comprar imgressos. O empenho e a definição do que irá compor a atividade também faz parte da avaliação. As implementações devem ser executadas no console e esse processo deve ser demonstrado na apresentacao.




cliente1.comprar_ingresso(ingresso1)
sala1.vender_ingresso(ingresso1)

from sala import Sala
from ingresso import Ingresso
from filme import Filme
from pessoa import Pessoa
from cliente import Cliente
from sessao import Sessao

cliente = Cliente("email", 5555, 55555, 55555, 55555 ,5555)
sala = Sala(11, 1)
filme = Filme(111, 22, 444)
ingresso = Ingresso(filme, 22, 33)
ingresso = Ingresso(filme, 22, 33)
sessao = Sessao(filme, 11, 11)