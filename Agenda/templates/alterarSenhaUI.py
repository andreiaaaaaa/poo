import streamlit as st
from views import View
import time

class AlterarSenhaUI:
    def main():
        st.header("Alterar Senha do Admin")

        nova = st.text_input("Nova senha", type="password")
        confirmar = st.text_input("Confirmar nova senha", type="password")

        if st.button("Alterar"):
            if nova != confirmar:
                st.error("As senhas não coincidem!")
            else:
                admin = View.cliente_listar_email("admin")
                View.cliente_atualizar(admin.get_id(), admin.get_nome(), admin.get_email(), admin.get_fone(), nova)
                st.success("Senha alterada com sucesso!")
                time.sleep(2)
                st.rerun()
