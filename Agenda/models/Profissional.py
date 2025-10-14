class Profissional:
    def __init__(self, id, nome, especialidade):
        self.set_id(id)
        self.set_nome(nome)
        self.set_especialidade(especialidade)

    def __str__(self):
        return f"{self.__id} - {self.__nome} ({self.__especialidade})"

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_especialidade(self): return self.__especialidade

    def set_id(self, id): self.__id = id
    def set_nome(self, nome): self.__nome = nome
    def set_especialidade(self, especialidade): self.__especialidade = especialidade

    def to_json(self):
        return {"id": self.__id, "nome": self.__nome, "especialidade": self.__especialidade}

    @staticmethod
    def from_json(dic):
        return Profissional(dic["id"], dic["nome"], dic["especialidade"])

    def __init__(self, id_profissional=0, nome="", especialidade="", telefone="", email=""):
        self.__id_profissional = id_profissional
        self.__nome = nome
        self.__especialidade = especialidade
        self.__telefone = telefone
        self.__email = email

    def get_id_profissional(self):
        return self.__id_profissional

    def set_id_profissional(self, id_profissional):
        self.__id_profissional = id_profissional

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_especialidade(self):
        return self.__especialidade

    def set_especialidade(self, especialidade):
        self.__especialidade = especialidade

    def get_telefone(self):
        return self.__telefone

    def set_telefone(self, telefone):
        self.__telefone = telefone

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def __str__(self):
        return f"{self.__id_profissional} - {self.__nome} ({self.__especialidade})"

