import json
from models.profissional import Profissional

class ProfissionalDAO:
    __arquivo = "profissionais.json"
    __objetos = []

    @classmethod
    def inserir(cls, p):
        cls.abrir()
        cls.__objetos.append(p)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.__objetos

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for p in cls.__objetos:
            if p.get_id() == id:
                return p
        return None

    @classmethod
    def atualizar(cls, p):
        cls.abrir()
        for i, obj in enumerate(cls.__objetos):
            if obj.get_id() == p.get_id():
                cls.__objetos[i] = p
        cls.salvar()

    @classmethod
    def excluir(cls, p):
        cls.abrir()
        cls.__objetos = [obj for obj in cls.__objetos if obj.get_id() != p.get_id()]
        cls.salvar()

    @classmethod
    def salvar(cls):
        with open(cls.__arquivo, "w") as f:
            json.dump(cls.__objetos, f, default=Profissional.to_json)

    @classmethod
    def abrir(cls):
        cls.__objetos = []
        try:
            with open(cls.__arquivo, "r") as f:
                lista = json.load(f)
                for d in lista:
                    cls.__objetos.append(Profissional.from_json(d))
        except FileNotFoundError:
            pass