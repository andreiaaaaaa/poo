import streamlit as st
from views import View
from datetime import datetime, timedelta
import time

class AbrirMinhaAgendaUI:
    def main():
        st.header("Abrir Minha Agenda")

        if "usuario_id" not in st.session_state or st.session_state.get("usuario_tipo") != "profissional":
            st.info("Você precisa entrar como profissional para abrir sua agenda.")
            return

        data = st.date_input("Data do atendimento", datetime.now().date())
        hora_inicio = st.time_input("Hora inicial")
        hora_fim = st.time_input("Hora final")
        intervalo = st.number_input("Intervalo (minutos)", min_value=5, max_value=180, value=30, step=5)

        if st.button("Confirmar"):
            inicio = datetime.combine(data, hora_inicio)
            fim = datetime.combine(data, hora_fim)
            if inicio >= fim:
                st.error("Hora inicial deve ser anterior à hora final.")
                return
            if intervalo <= 0:
                st.error("Intervalo deve ser positivo.")
                return

            atual = inicio
            count = 0
            while atual < fim:
                View.horario_inserir(atual, False, None, None, st.session_state["usuario_id"])
                atual = atual + timedelta(minutes=intervalo)
                count += 1

            st.success(f"{count} horários inseridos na sua agenda.")
            time.sleep(1)
            st.rerun()
