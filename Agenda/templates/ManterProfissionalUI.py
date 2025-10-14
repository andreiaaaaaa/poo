import streamlit as st
import pandas as pd
from views import View

class ManterProfissionalUI:
    def main():
        st.header("Cadastro de Profissionais")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterProfissionalUI.listar()
        with tab2: ManterProfissionalUI.inserir()
        with tab3: ManterProfissionalUI.atualizar()
        with tab4: ManterProfissionalUI.excluir()

    def listar():
        lista = View.profissional_listar()
        if len(lista) == 0:
            st.write("Nenhum profissional cadastrado")
        else:
            dic = [{"id": p.get_id(), "nome": p.get_nome(), "especialidade": p.get_especialidade()} for p in lista]
            st.dataframe(pd.DataFrame(dic))

    def inserir():
        nome = st.text_input("Nome")
        especialidade = st.text_input("Especialidade")
        if st.button("Inserir"):
            View.profissional_inserir(nome, especialidade)
            st.success("Profissional inserido com sucesso")

    def atualizar():
        lista = View.profissional_listar()
        if len(lista) == 0:
            st.write("Nenhum profissional cadastrado")
        else:
            p = st.selectbox("Selecione o profissional", lista)
            nome = st.text_input("Novo nome", p.get_nome())
            especialidade = st.text_input("Nova especialidade", p.get_especialidade())
            if st.button("Atualizar"):
                View.profissional_atualizar(p.get_id(), nome, especialidade)
                st.success("Profissional atualizado")

    def excluir():
        lista = View.profissional_listar()
        if len(lista) == 0:
            st.write("Nenhum profissional cadastrado")
        else:
            p = st.selectbox("Selecione o profissional para excluir", lista)
            if st.button("Excluir"):
                View.profissional_excluir(p.get_id())
                st.success("Profissional excluído")

from Profissional import Profissional
from ProfissionalDAO import profissionalDAO # type: ignore

class ManterProfissionalUI:
    def __init__(self):
        self.__dao = profissionalDAO()

    def menu(self):
        while True:
            print("\n--- Cadastro de Profissionais ---")
            print("1 - Cadastrar Profissional")
            print("2 - Listar Profissionais")
            print("3 - Atualizar Profissional")
            print("4 - Excluir Profissional")
            print("0 - Voltar")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.cadastrar()
            elif opcao == "2":
                self.listar()
            elif opcao == "3":
                self.atualizar()
            elif opcao == "4":
                self.excluir()
            elif opcao == "0":
                break
            else:
                print("Opção inválida!")

    def cadastrar(self):
        nome = input("Nome: ")
        especialidade = input("Especialidade: ")
        telefone = input("Telefone: ")
        email = input("Email: ")
        profissional = profissional(0, nome, especialidade, telefone, email)
        self.__dao.inserir(profissional)
        print("✅ Profissional cadastrado com sucesso!")

    def listar(self):
        print("\n--- Lista de Profissionais ---")
        for p in self.__dao.listar():
            print(p)

    def atualizar(self):
        self.listar()
        id_profissional = int(input("\nDigite o ID do profissional que deseja atualizar: "))
        profissional = self.__dao.buscar_por_id(id_profissional)
        if profissional:
            nome = input(f"Novo nome ({profissional.get_nome()}): ") or profissional.get_nome()
            especialidade = input(f"Nova especialidade ({profissional.get_especialidade()}): ") or profissional.get_especialidade()
            telefone = input(f"Novo telefone ({profissional.get_telefone()}): ") or profissional.get_telefone()
            email = input(f"Novo email ({profissional.get_email()}): ") or profissional.get_email()

            profissional.set_nome(nome)
            profissional.set_especialidade(especialidade)
            profissional.set_telefone(telefone)
            profissional.set_email(email)

            self.__dao.atualizar(profissional)
            print("✅ Profissional atualizado com sucesso!")
        else:
            print("❌ Profissional não encontrado!")

    def excluir(self):
        self.listar()
        id_profissional = int(input("\nDigite o ID do profissional que deseja excluir: "))
        if self.__dao.excluir(id_profissional):
            print("✅ Profissional excluído com sucesso!")
        else:
            print("❌ Profissional não encontrado!")
