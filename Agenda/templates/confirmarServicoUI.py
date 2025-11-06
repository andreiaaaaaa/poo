import streamlit as st
from views import View
import time

class ConfirmarServicoUI:
    def main():
        st.header("Confirmar Serviços Agendados")

        if "usuario_id" not in st.session_state or st.session_state.get("usuario_tipo") != "profissional":
            st.info("Acesse como profissional para confirmar serviços.")
            return

        prof_id = st.session_state["usuario_id"]
        horarios = View.horario_listar()

        pendentes = [h for h in horarios if h.get_id_profissional() == prof_id and not h.get_confirmado() and h.get_id_cliente()]

        if len(pendentes) == 0:
            st.info("Nenhum serviço pendente de confirmação.")
            return

        opc = st.selectbox("Horários pendentes", pendentes, format_func=lambda x: x.get_data().strftime("%d/%m/%Y %H:%M"))
        if st.button("Confirmar Serviço"):
            View.horario_atualizar(opc.get_id(), opc.get_data(), True, opc.get_id_cliente(), opc.get_id_servico(), opc.get_id_profissional())
            st.success("Serviço confirmado.")
            time.sleep(1)
            st.rerun()