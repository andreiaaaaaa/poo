import streamlit as st
from views import View

class VisualizarMinhaAgendaUI:
    def main():
        st.header("Minha Agenda de Atendimentos")

        horarios = View.horario_listar()
        achou = False

        for h in horarios:
            if h.get_id_profissional() == st.session_state["usuario_id"]:
                achou = True
                cliente = View.cliente_listar_id(h.get_id_cliente()) if h.get_id_cliente() else None
                servico = View.servico_listar_id(h.get_id_servico()) if h.get_id_servico() else None

                st.write(f"📅 {h.get_data().strftime('%d/%m/%Y %H:%M')}")
                st.write(f"👤 Cliente: {cliente.get_nome() if cliente else 'Disponível'}")
                st.write(f"💈 Serviço: {servico.get_descricao() if servico else '-'}")
                st.write(f"✅ Confirmado: {'Sim' if h.get_confirmado() else 'Não'}")
                st.markdown("---")

        if not achou:
            st.info("Você ainda não tem horários cadastrados.")