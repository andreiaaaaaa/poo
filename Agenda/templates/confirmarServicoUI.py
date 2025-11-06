import streamlit as st
from views import View
import time

class ConfirmarServicoUI:
    def main():
        st.header("Confirmar Serviços Agendados")

        horarios = View.horario_listar()
        lista = [h for h in horarios if h.get_id_profissional() == st.session_state["usuario_id"] and not h.get_confirmado() and h.get_id_cliente()]

        if len(lista) == 0:
            st.write("Nenhum serviço pendente de confirmação.")
        else:
            horario = st.selectbox("Selecione um horário", lista)
            if st.button("Confirmar Serviço"):
                View.horario_atualizar(
                    horario.get_id(),
                    horario.get_data(),
                    True,
                    horario.get_id_cliente(),
                    horario.get_id_servico(),
                    horario.get_id_profissional()
                )
                st.success("Serviço confirmado com sucesso!")
                time.sleep(2)
                st.rerun()