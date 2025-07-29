from datetime import datetime

class Contato:
    def __init__(self, id, nome, email, telefone, nascimento):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.nascimento = nascimento

    def __str__(self):
        return (f"ID: {self.id}\nNome: {self.nome}\nEmail: {self.email}\n"
                f"Telefone: {self.telefone}\nNascimento: {self.nascimento}")

    def get_id(self):
        return self.id

    def get_nome(self):
        return self.nome

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def set_email(self, novo_email):
        self.email = novo_email

    def set_telefone(self, novo_telefone):
        self.telefone = novo_telefone

    def set_nascimento(self, nova_data):
        self.nascimento = datetime.strptime(nova_data, "%d/%m/%Y")
import pickle

class ContatoUI:
    def __init__(self):
        self.contatos = {}

    def menu(self):
        while True:
            print("\n--- Menu da Agenda ---")
            print("1. Inserir contato")
            print("2. Listar todos os contatos")
            print("3. Listar contato por ID")
            print("4. Atualizar contato")
            print("5. Excluir contato")
            print("6. Pesquisar por iniciais do nome")
            print("7. Listar aniversariantes do mês")
            print("8. Abrir arquivo")
            print("9. Salvar arquivo")
            print("0. Sair")
            op = input("Escolha uma opção: ")

            if op == "1":
                self.inserir()
            elif op == "2":
                self.listar()
            elif op == "3":
                self.listar_id()
            elif op == "4":
                self.atualizar()
            elif op == "5":
                self.excluir()
            elif op == "6":
                self.pesquisar()
            elif op == "7":
                self.aniversariantes()
            elif op == "8":
                self.abrir()
            elif op == "9":
                self.salvar()
            elif op == "0":
                print("Saindo...")
                break
            else:
                print("Opção inválida!")

    def inserir(self):
        id = input("ID: ")
        nome = input("Nome: ")
        email = input("Email: ")
        telefone = input("Telefone: ")
        nascimento = input("Data de nascimento (dd/mm/aaaa): ")
        contato = Contato(id, nome, email, telefone, nascimento)
        self.contatos[id] = contato
        print("Contato adicionado com sucesso!")

    def listar(self):
        if not self.contatos:
            print("Agenda vazia!")
        for contato in self.contatos.values():
            print("-" * 30)
            print(contato)

    def listar_id(self):
        id = input("Digite o ID do contato: ")
        contato = self.contatos.get(id)
        if contato:
            print(contato)
        else:
            print("Contato não encontrado!")

    def atualizar(self):
        id = input("Digite o ID do contato que deseja atualizar: ")
        if id in self.contatos:
            nome = input("Novo nome: ")
            email = input("Novo email: ")
            telefone = input("Novo telefone: ")
            nascimento = input("Nova data de nascimento (dd/mm/aaaa): ")
            contato = self.contatos[id]
            contato.set_nome(nome)
            contato.set_email(email)
            contato.set_telefone(telefone)
            contato.set_nascimento(nascimento)
            print("Contato atualizado com sucesso!")
        else:
            print("Contato não encontrado!")

    def excluir(self):
        id = input("Digite o ID do contato a ser excluído: ")
        if id in self.contatos:
            del self.contatos[id]
            print("Contato removido!")
        else:
            print("Contato não encontrado!")

    def pesquisar(self):
        prefixo = input("Digite as iniciais do nome: ").lower()
        achou = False
        for contato in self.contatos.values():
            if contato.get_nome().lower().startswith(prefixo):
                print(contato)
                achou = True
        if not achou:
            print("Nenhum contato encontrado com esse prefixo!")

    def aniversariantes(self):
        mes = int(input("Digite o número do mês (1 a 12): "))
        for contato in self.contatos.values():
            if contato.nascimento.month == mes:
                print(contato)

    def salvar(self):
        with open("contatos.py", "wb") as f:
            pickle.dump(self.contatos, f)
        print("Contatos salvos com sucesso!")

    def abrir(self):
        try:
            with open("contatos.pkl", "rb") as f:
                self.contatos = pickle.load(f)
            print("Contatos carregados com sucesso!")
        except FileNotFoundError:
            print("Arquivo não encontrado!")
           
if __name__ == "__main__":
    app = ContatoUI()
    app.menu()