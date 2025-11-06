from datetime import datetime

class Horario:
    def __init__(self, id, data, confirmado, id_cliente, id_servico, id_profissional):
        self.__id = id
        self.__data = data
        self.__confirmado = confirmado
        self.__id_cliente = id_cliente
        self.__id_servico = id_servico
        self.__id_profissional = id_profissional

    def __str__(self):
        return f"{self.__id} - {self.__data} - {self.__confirmado} - {self.__id_cliente} - {self.__id_servico} - {self.__id_profissional}"


    def get_id(self): return self.__id
    def get_data(self): return self.__data
    def get_confirmado(self): return self.__confirmado
    def get_id_cliente(self): return self.__id_cliente
    def get_id_servico(self): return self.__id_servico
    def get_id_profissional(self): return self.__id_profissional

    def set_id(self, id): self.__id = id
    def set_data(self, data): self.__data = data
    def set_confirmado(self, confirmado): self.__confirmado = confirmado
    def set_id_cliente(self, id_cliente): self.__id_cliente = id_cliente
    def set_id_servico(self, id_servico): self.__id_servico = id_servico
    def set_id_profissional(self, id_profissional): self.__id_profissional = id_profissional

    def to_json(self):
        return {
            "id": self.__id,
            "data": self.__data.strftime("%Y-%m-%d %H:%M:%S"),
            "confirmado": self.__confirmado,
            "id_cliente": self.__id_cliente,
            "id_servico": self.__id_servico,
            "id_profissional": self.__id_profissional
        }

    @staticmethod
    def from_json(dic):
        data = datetime.strptime(dic["data"], "%Y-%m-%d %H:%M:%S")
        return Horario(dic["id"], data, dic["confirmado"],
                       dic["id_cliente"], dic["id_servico"], dic["id_profissional"])