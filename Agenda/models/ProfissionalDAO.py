import json
from models.Profissional import Profissional

class ProfissionalDAO:
    __objetos = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for aux in cls.__objetos:
            if aux.get_id() > id: id = aux.get_id()
        obj.set_id(id + 1)
        cls.__objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.__objetos

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls.__objetos:
            if obj.get_id() == id: return obj
        return None

    @classmethod
    def atualizar(cls, obj):
        aux = cls.listar_id(obj.get_id())
        if aux != None:
            cls.__objetos.remove(aux)
            cls.__objetos.append(obj)
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        aux = cls.listar_id(obj.get_id())
        if aux != None:
            cls.__objetos.remove(aux)
            cls.salvar()

    @classmethod
    def abrir(cls):
        cls.__objetos = []
        try:
            with open("profissionais.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    cls.__objetos.append(Profissional.from_json(dic))
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("profissionais.json", mode="w") as arquivo:
            json.dump(cls.__objetos, arquivo, default=Profissional.to_json)

from Profissional import Profissional

class ProfissionalDAO:
    def __init__(self):
        self.__lista_profissionais = []
        self.__id_atual = 1

    def inserir(self, profissional):
        profissional.set_id_profissional(self.__id_atual)
        self.__id_atual += 1
        self.__lista_profissionais.append(profissional)

    def listar(self):
        return self.__lista_profissionais

    def buscar_por_id(self, id_profissional):
        for p in self.__lista_profissionais:
            if p.get_id_profissional() == id_profissional:
                return p
        return None

    def atualizar(self, profissional):
        for i, p in enumerate(self.__lista_profissionais):
            if p.get_id_profissional() == profissional.get_id_profissional():
                self.__lista_profissionais[i] = profissional
                return True
        return False

    def excluir(self, id_profissional):
        for p in self.__lista_profissionais:
            if p.get_id_profissional() == id_profissional:
                self.__lista_profissionais.remove(p)
                return True
        return False
