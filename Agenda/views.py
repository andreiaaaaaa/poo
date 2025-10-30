from models.cliente import Cliente
from models.clienteDAO import ClienteDAO
from models.servico import Servico
from models.servicoDAO import ServicoDAO
from models.profissional import Profissional
from models.profissionalDAO import ProfissionalDAO
from models.horario import Horario
from models.horarioDAO import HorarioDAO


class View:

    def cliente_listar():
        return ClienteDAO.listar()

    def cliente_listar_id(id):
        return ClienteDAO.listar_id(id)

    def cliente_inserir(nome, email, fone, senha):
        cliente = Cliente(0, nome, email, fone, senha)
        ClienteDAO.inserir(cliente)

    def cliente_atualizar(id, nome, email, fone, senha):
        cliente = Cliente(id, nome, email, fone, senha)
        ClienteDAO.atualizar(cliente)

    def cliente_excluir(id):
        cliente = Cliente(id, "", "", "", "",)
        ClienteDAO.excluir(cliente)

    def cliente_criar_admin():
        for c in View.cliente_listar():
            if c.get_email() == "admin":
                return
        View.cliente_inserir("admin", "admin", "fone", "1234")

    def cliente_autenticar(email, senha):
        for c in View.cliente_listar():
            if c.get_email() == email and c.get_senha() == senha:
                return {"id": c.get_id(), "nome": c.get_nome()}
        return None

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

    def horario_inserir(data, confirmado, id_cliente, id_servico, id_profissional):
        c = Horario(0, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        c.set_id_profissional(id_profissional) 
        HorarioDAO.inserir(c)

    def horario_listar():
        return HorarioDAO.listar()

    def horario_atualizar(id, data, confirmado, id_cliente, id_servico):
        c = Horario(id, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        c.set_id_profissional(id_profissional=Profissional)  

        HorarioDAO.atualizar(c)

    def horario_excluir(id):
        c = Horario(id, None)
        HorarioDAO.excluir(c)

    def profissional_inserir(nome, especialidade):
        p = Profissional(0, nome, especialidade)
        ProfissionalDAO.inserir(p)

    def profissional_listar():
        return ProfissionalDAO.listar()

    def profissional_listar_id(id):
        return ProfissionalDAO.listar_id(id)

    def profissional_atualizar(id, nome, especialidade):
        p = Profissional(id, nome, especialidade)
        ProfissionalDAO.atualizar(p)

    def profissional_excluir(id):
        p = Profissional(id, "", "")
        ProfissionalDAO.excluir(p)
