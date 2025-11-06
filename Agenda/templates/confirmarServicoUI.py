import streamlit as st
from views import View
import time

class AlterarSenhaUI:
    def main():
        st.header("Alterar senha (Admin)")

        if "usuario_id" not in st.session_state or st.session_state.get("usuario_nome") != "admin":
            st.info("Somente o Admin pode alterar sua senha aqui.")
            return

        nova = st.text_input("Nova senha", type="password")
        confirma = st.text_input("Confirmar nova senha", type="password")

        if st.button("Alterar"):
            if nova.strip() == "":
                st.error("Senha não pode ser vazia.")
                return
            if nova != confirma:
                st.error("Senhas não conferem.")
                return

            admin = None
            for c in View.cliente_listar():
                if c.get_email().lower() == "admin":
                    admin = c
                    break

            if not admin:
                st.error("Admin não encontrado.")
                return

            View.cliente_atualizar(admin.get_id(), admin.get_nome(), admin.get_email(), admin.get_fone(), nova)
            st.success("Senha do admin alterada com sucesso.")
            time.sleep(1)
            st.rerun()