class PaisUI:
    def __init__(self):
        self.paises = []

    def menu(self):
        print("\nMenu - Cadastro de Países:")
        print("1. Inserir país")
        print("2. Listar países")
        print("3. Atualizar país")
        print("4. Excluir país")
        print("5. Mostrar país mais populoso")
        print("6. Mostrar país mais povoado (maior densidade)")
        print("7. Sair")

    def inserir(self):
        id = input("ID: ")
        nome = input("Nome: ")
        populacao = int(input("População: "))
        area = float(input("Área (em km²): "))
        pais = Pais(id, nome, populacao, area)
        self.paises.append(pais)
        print("País inserido com sucesso.")

    def listar(self):
        if not self.paises:
            print("Nenhum país cadastrado.")
        else:
            for p in self.paises:
                print(p)

    def atualizar(self):
        id = input("Digite o ID do país a ser atualizado: ")
        for p in self.paises:
            if p.id == id:
                p.nome = input("Novo nome: ")
                p.populacao = int(input("Nova população: "))
                p.area = float(input("Nova área: "))
                print("País atualizado.")
                return
        print("País não encontrado.")

    def excluir(self):
        id = input("Digite o ID do país a ser excluído: ")
        for p in self.paises:
            if p.id == id:
                self.paises.remove(p)
                print("País removido.")
                return
        print("País não encontrado.")

    def mais_populoso(self):
        if not self.paises:
            print("Nenhum país cadastrado.")
            return
        mais_pop = max(self.paises, key=lambda p: p.populacao)
        print("País mais populoso:")
        print(mais_pop)

    def mais_povoado(self):
        if not self.paises:
            print("Nenhum país cadastrado.")
            return
        mais_pov = max(self.paises, key=lambda p: p.densidade())
        print("País mais povoado (maior densidade):")
        print(mais_pov)
        print(f"Densidade: {mais_pov.densidade():.2f} hab/km²")

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
                self.mais_populoso()
            elif opcao == '6':
                self.mais_povoado()
            elif opcao == '7':
                print("Encerrando o cadastro.")
                break
            else:
                print("Opção inválida.")

if __name__ == "__main__":
    ui = PaisUI()
    ui.main()