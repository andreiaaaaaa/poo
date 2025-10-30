import streamlit as st 
from templates.manterClienteUI import ManterClienteUI
from templates.manterServicoUI import ManterServicoUI
from templates.manterHorarioUI import ManterHorarioUI
from templates.manterProfissionalUI import ManterProfissionalUI


class IndexUI:
    def menu_admin():
        op = st.sidebar.selectbox("Menu", [
            "Cadastro de Clientes",
            "Cadastro de Serviços",
            "Cadastro de Profissionais",
            "Cadastro de Horários"
        ])
        if op == "Cadastro de Clientes": ManterClienteUI.main()
        if op == "Cadastro de Serviços": ManterServicoUI.main()
        if op == "Cadastro de Profissionais": ManterProfissionalUI.main()
        if op == "Cadastro de Horários": ManterHorarioUI.main()
IndexUI.menu_admin()
        