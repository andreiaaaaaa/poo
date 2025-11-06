import streamlit as st
import time
from views import View
import pandas as pd

class ManterProfissionalUI:
    def main():
        st.header("Cadastro de Profissionais")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterProfissionalUI.listar()
        with tab2: ManterProfissionalUI.inserir()
        with tab3: ManterProfissionalUI.atualizar()
        with tab4: ManterProfissionalUI.excluir()

    def listar():
        clientes = View.profissional_listar()
        if len(clientes) == 0:
            st.write("Nenhum Profissional cadastrado")
        else:
            list_dic = []
            for obj in clientes:
                list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)

    def inserir():
        nome = st.text_input("Nome")
        email = st.text_input("E-mail")
        fone = st.text_input("Fone")
        senha = st.text_input("Senha", type="password")
        especialidade = st.text_input("Especialidade")


        if st.button("Inserir"):
            View.profissional_inserir(nome, email, fone, senha, especialidade)
            st.success("Profissional inserido com sucesso")
            time.sleep(2)
            st.rerun()

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