from models.cliente import Cliente
from models.clienteDAO import ClienteDAO
from models.servico import Servico
from models.servicoDAO import ServicoDAO
from models.horario import Horario
from models.HorarioDAO import HorarioDAO

class View:

    def cliente_listar():
        return ClienteDAO.listar()

    def cliente_listar_id(id):
        return ClienteDAO.listar_id(id)

    def cliente_inserir(nome, email, fone):
        cliente = Cliente(0, nome, email, fone)
        ClienteDAO.inserir(cliente)

    def cliente_atualizar(id, nome, email, fone):
        cliente = Cliente(id, nome, email, fone)
        ClienteDAO.atualizar(cliente)

    def cliente_excluir(id):
        cliente = Cliente(id, "", "", "")
        ClienteDAO.excluir(cliente)

    def servico_listar():
        return ServicoDAO.listar()

    def servico_listar_id(id):
        return ServicoDAO.listar_id(id)

    def servico_inserir(descricao, valor):
        servico = Servico(0, descricao, valor)
        ServicoDAO.inserir(servico)

    def servico_atualizar(id, descricao, valor):
        servico = Servico(id, descricao, valor)
        ServicoDAO.atualizar(servico)

    def servico_excluir(id):
        servico = Servico(id, "", 0.0)
        ServicoDAO.excluir(servico)

    def horario_inserir(data, confirmado, id_cliente, id_servico):
        c = Horario(0, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        HorarioDAO.inserir(c)

    def horario_listar():
        return HorarioDAO.listar()

    def horario_atualizar(id, data, confirmado, id_cliente, id_servico):
        c = Horario(id, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        HorarioDAO.atualizar(c)

    def horario_excluir(id):
        c = Horario(id, None)
        HorarioDAO.excluir(c)

from ManterProfissionalUI import ManterProfissionalUI # type: ignore

class View:
    def __init__(self):
        self.__manter_profissional_ui = ManterProfissionalUI()

    def menu_principal(self):
        while True:
            print("\n=== Sistema de Agendamento de Serviços ===")
            print("1 - Cadastro de Clientes")
            print("2 - Cadastro de Profissionais")
            print("3 - Cadastro de Horários")
            print("0 - Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                print("→ Abrindo cadastro de clientes...")
            elif opcao == "2":
                self.__manter_profissional_ui.menu()
            elif opcao == "3":
                print("→ Abrindo cadastro de horários...")
            elif opcao == "0":
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida!")
