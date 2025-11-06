import streamlit as st
from views import View
from datetime import datetime, timedelta
import time

class AbrirMinhaAgendaUI:
    def main():
        st.header("Abrir Minha Agenda")

        data = st.date_input("Data do atendimento", datetime.now())
        hora_inicial = st.time_input("Hora inicial")
        hora_final = st.time_input("Hora final")
        intervalo = st.number_input("Intervalo (minutos)", min_value=10, max_value=120, step=10)

        if st.button("Confirmar"):
            hora_atual = datetime.combine(data, hora_inicial)
            fim = datetime.combine(data, hora_final)
            while hora_atual < fim:
                View.horario_inserir(
                    hora_atual,
                    False,
                    None, None,
                    st.session_state["usuario_id"]
                )
                hora_atual += timedelta(minutes=intervalo)
            st.success("Horários inseridos com sucesso!")
            time.sleep(2)
            st.rerun()