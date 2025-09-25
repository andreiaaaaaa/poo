from templates.ManterClienteUI import ManterClienteUI
from templates.ManterServicoUI import ManterServicoUI

import streamlit as st # type: ignore

class IndexUI:
    def main():
        st.sidebar.title("Menu")
        op = st.sidebar.selectbox("Escolha uma opção", ["Clientes", "Serviços"])

        if op == "Clientes":
            ManterClienteUI.main()
        elif op == "Serviços":
            ManterServicoUI.main()

IndexUI.main()