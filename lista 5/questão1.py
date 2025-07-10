from datetime import datetime

class Paciente:
    def __init__(self, nome, cpf, telefone, nascimento):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__nascimento = datetime.strptime(nascimento, "%d/%m/%Y")
    
    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome

    def get_cpf(self):
        return self.__cpf

    def set_cpf(self, cpf):
        self.__cpf = cpf

    def get_telefone(self):
        return self.__telefone

    def set_telefone(self, telefone):
        self.__telefone = telefone

    def get_nascimento(self):
        return self.__nascimento.strftime("%d/%m/%Y")

    def set_nascimento(self, nascimento):
        self.__nascimento = datetime.strptime(nascimento, "%d/%m/%Y")

    def idade(self):
        hoje = datetime.today()
        anos = hoje.year - self.__nascimento.year
        meses = hoje.month - self.__nascimento.month
        if hoje.day < self.__nascimento.day:
            meses -= 1
        if meses < 0:
            anos -= 1
            meses += 12
        return f"{anos} anos e {meses} meses"

    def __str__(self):
        return f"Nome: {self.__nome}, CPF: {self.__cpf}, Telefone: {self.__telefone}, Nascimento: {self.get_nascimento()}, Idade: {self.idade()}"

def ui_paciente():
    print("Cadastro de Paciente")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    telefone = input("Telefone: ")
    nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    
    paciente = Paciente(nome, cpf, telefone, nascimento)
    
    print("\nDados do paciente:")
    print(paciente)

if __name__ == "__main__":
    ui_paciente()

