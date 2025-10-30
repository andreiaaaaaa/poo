import streamlit as st
from views import View
import time

class PerfilProfissionalUI:
    def main():
        st.header("Meus Dados (Profissional)")

        p = View.profissional_listar_id(st.session_state["usuario_id"])
        nome = st.text_input("Nome", p.get_nome())
        email = st.text_input("E-mail", p.get_email())
        fone = st.text_input("Fone", p.get_fone())
        senha = st.text_input("Senha", p.get_senha(), type="password")
        especialidade = st.text_input("Especialidade", p.get_especialidade())

        if st.button("Atualizar"):
            View.profissional_atualizar(p.get_id(), nome, email, fone, senha, especialidade)
            st.success("Dados atualizados!")
            time.sleep(2)
            st.rerun()

