
from templates.ManterProfissionalUI import ManterProfissionalUI

class View:
    def __init__(self):
        self.__manter_profissional_ui = ManterProfissionalUI()

    def menu_principal(self):
        while True:
            print("\n=== Sistema de Agendamento de Serviços ===")
            print("1 - Cadastro de Clientes")
            print("2 - Cadastro de Profissionais")
            print("3 - Cadastro de Horários")
            print("0 - Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                print("→ Abrindo cadastro de clientes...")
            elif opcao == "2":
                self.__manter_profissional_ui.menu()
            elif opcao == "3":
                print("→ Abrindo cadastro de horários...")
            elif opcao == "0":
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida!")
