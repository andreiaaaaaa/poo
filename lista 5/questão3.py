from datetime import datetime

class Contato:
    def __init__(self, id, nome, email, telefone, data_nascimento):
        self._id = id
        self._nome = nome
        self._email = email
        self._telefone = telefone
        self._data_nascimento = data_nascimento

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    def get_telefone(self):
        return self._telefone

    def set_telefone(self, telefone):
        self._telefone = telefone

    def get_data_nascimento(self):
        return self._data_nascimento

    def set_data_nascimento(self, data_nascimento):
        self._data_nascimento = data_nascimento

    def __str__(self):
        return (f"ID: {self._id}\n"
                f"Nome: {self._nome}\n"
                f"E-mail: {self._email}\n"
                f"Telefone: {self._telefone}\n"
                f"Data de Nascimento: {self._data_nascimento}")

class ContatoUI:
    def __init__(self):
        self.contatos = []
        self.next_id = 1

    def menu(self):
        print("\n--- Agenda de Contatos ---")
        print("1. Inserir novo contato")
        print("2. Listar todos os contatos")
        print("3. Atualizar contato")
        print("4. Excluir contato")
        print("5. Pesquisar contato pelas iniciais do nome")
        print("6. Aniversariantes do mês")
        print("7. Sair")

    def inserir(self):
        nome = input("Nome: ")
        email = input("E-mail: ")
        telefone = input("Telefone: ")
        data_nascimento = input("Data de nascimento (dd/mm/yyyy): ")
        contato = Contato(self.next_id, nome, email, telefone, data_nascimento)
        self.contatos.append(contato)
        self.next_id += 1
        print("Contato inserido com sucesso.")

    def listar(self):
        if not self.contatos:
            print("Nenhum contato cadastrado.")
        else:
            for contato in self.contatos:
                print(contato)
                print("-" * 20)

    def atualizar(self):
        id = int(input("Informe o ID do contato a ser atualizado: "))
        contato = next((c for c in self.contatos if c.get_id() == id), None)
        if contato:
            nome = input(f"Novo nome ({contato.get_nome()}): ") or contato.get_nome()
            email = input(f"Novo e-mail ({contato.get_email()}): ") or contato.get_email()
            telefone = input(f"Novo telefone ({contato.get_telefone()}): ") or contato.get_telefone()
            data_nascimento = input(f"Nova data de nascimento ({contato.get_data_nascimento()}): ") or contato.get_data_nascimento()
            contato.set_nome(nome)
            contato.set_email(email)
            contato.set_telefone(telefone)
            contato.set_data_nascimento(data_nascimento)
            print("Contato atualizado com sucesso.")
        else:
            print("Contato não encontrado.")

    def excluir(self):
        id = int(input("Informe o ID do contato a ser excluído: "))
        for i, contato in enumerate(self.contatos):
            if contato.get_id() == id:
                del self.contatos[i]
                print("Contato excluído com sucesso.")
                return
        print("Contato não encontrado.")

    def pesquisar(self):
        iniciais = input("Digite as iniciais do nome: ").lower()
        encontrados = [c for c in self.contatos if c.get_nome().lower().startswith(iniciais)]
        if encontrados:
            for contato in encontrados:
                print(contato)
                print("-" * 20)
        else:
            print("Nenhum contato encontrado com essas iniciais.")

    def aniversariantes(self):
        mes = input("Digite o mês (1-12): ")
        try:
            mes = int(mes)
            encontrados = []
            for contato in self.contatos:
                try:
                    data = datetime.strptime(contato.get_data_nascimento(), "%d/%m/%Y")
                    if data.month == mes:
                        encontrados.append(contato)
                except ValueError:
                    continue
            if encontrados:
                for contato in encontrados:
                    print(contato)
                    print("-" * 20)
            else:
                print("Nenhum aniversariante neste mês.")
        except ValueError:
            print("Mês inválido.")

    def main(self):
        while True:
            self.menu()
            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                self.inserir()
            elif opcao == "2":
                self.listar()
            elif opcao == "3":
                self.atualizar()
            elif opcao == "4":
                self.excluir()
            elif opcao == "5":
                self.pesquisar()
            elif opcao == "6":
                self.aniversariantes()
            elif opcao == "7":
                print("Saindo da agenda.")
                break
            else:
                print("Opção inválida.")

if __name__ == "__main__":
    ui = ContatoUI()
    ui.main()