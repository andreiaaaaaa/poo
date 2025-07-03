class Contato:
    def __init__(self, id, nome, email, telefone):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def __str__(self):
        return f"{self.id} - {self.nome}, Email: {self.email}, Tel: {self.telefone}"

class ContatoUI:
    def __init__(self):
        self.contatos = []

    def menu(self):
        print("\n--- MENU DA AGENDA ---")
        print("1 - Inserir novo contato")
        print("2 - Listar contatos")
        print("3 - Atualizar contato")
        print("4 - Excluir contato")
        print("5 - Pesquisar por iniciais")
        print("6 - Sair")

    def inserir(self):
        id = input("ID: ")
        nome = input("Nome: ")
        email = input("Email: ")
        telefone = input("Telefone: ")
        novo = Contato(id, nome, email, telefone)
        self.contatos.append(novo)
        print("Contato adicionado com sucesso.")

    def listar(self):
        if not self.contatos:
            print("Agenda vazia.")
        for c in self.contatos:
            print(c)

    def atualizar(self):
        id = input("Informe o ID do contato a atualizar: ")
        for c in self.contatos:
            if c.id == id:
                c.nome = input("Novo nome: ")
                c.email = input("Novo email: ")
                c.telefone = input("Novo telefone: ")
                print("Contato atualizado.")
                return
        print("Contato não encontrado.")

    def excluir(self):
        id = input("Informe o ID do contato a excluir: ")
        for c in self.contatos:
            if c.id == id:
                self.contatos.remove(c)
                print("Contato removido.")
                return
        print("Contato não encontrado.")

    def pesquisar(self):
        iniciais = input("Digite as iniciais do nome: ").lower()
        encontrados = [c for c in self.contatos if c.nome.lower().startswith(iniciais)]
        if encontrados:
            for c in encontrados:
                print(c)
        else:
            print("Nenhum contato encontrado com essas iniciais.")

    def main(self):
        while True:
            self.menu()
            opcao = input("Escolha uma opção: ")
            if opcao == '1':
                self.inserir()
            elif opcao == '2':
                self.listar()
            elif opcao == '3':
                self.atualizar()
            elif opcao == '4':
                self.excluir()
            elif opcao == '5':
                self.pesquisar()
            elif opcao == '6':
                print("Encerrando a agenda. Até logo!")
                break
            else:
                print("Opção inválida.")

if __name__ == "__main__":
    ui = ContatoUI()
    ui.main()