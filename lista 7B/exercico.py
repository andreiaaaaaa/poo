class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def __str__(self):
        return f"{self.nome} - {self.telefone} - {self.email}"



class ContatoDAO:
    def __init__(self):
        self.contatos = []

    def adicionar(self, contato):
        self.contatos.append(contato)

    def listar(self):
        return self.contatos

    def buscar(self, nome):
        for contato in self.contatos:
            if contato.nome.lower() == nome.lower():
                return contato
        return None

    def remover(self, nome):
        contato = self.buscar(nome)
        if contato:
            self.contatos.remove(contato)
            return True
        return False



class ContatoView:
    def mostrar_menu(self):
        print("\n=== MENU ===")
        print("1 - Adicionar Contato")
        print("2 - Listar Contatos")
        print("3 - Buscar Contato")
        print("4 - Remover Contato")
        print("0 - Sair")

    def ler_dados_contato(self):
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        email = input("Email: ")
        return nome, telefone, email

    def mostrar_contato(self, contato):
        if contato:
            print(f"\nContato encontrado: {contato}")
        else:
            print("\nContato não encontrado.")

    def mostrar_contatos(self, contatos):
        print("\n--- Lista de Contatos ---")
        for contato in contatos:
            print(contato)

    def mostrar_mensagem(self, msg):
        print(msg)


class ContatoUI:
    def __init__(self):
        self.dao = ContatoDAO()
        self.view = ContatoView()

    def executar(self):
        while True:
            self.view.mostrar_menu()
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                nome, telefone, email = self.view.ler_dados_contato()
                contato = Contato(nome, telefone, email)
                self.dao.adicionar(contato)
                self.view.mostrar_mensagem("Contato adicionado com sucesso!")

            elif opcao == '2':
                contatos = self.dao.listar()
                self.view.mostrar_contatos(contatos)

            elif opcao == '3':
                nome = input("Digite o nome para buscar: ")
                contato = self.dao.buscar(nome)
                self.view.mostrar_contato(contato)

            elif opcao == '4':
                nome = input("Digite o nome para remover: ")
                if self.dao.remover(nome):
                    self.view.mostrar_mensagem("Contato removido com sucesso.")
                else:
                    self.view.mostrar_mensagem("Contato não encontrado.")

            elif opcao == '0':
                self.view.mostrar_mensagem("Saindo...")
                break

            else:
                self.view.mostrar_mensagem("Opção inválida.")



if __name__ == "__main__":
    ui = ContatoUI()
    ui.executar()
