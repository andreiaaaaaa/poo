import streamlit as st
from views import View

class VisualizarMeusServicosUI:
    def main():
        st.header("Meus Serviços Agendados")

        horarios = View.horario_listar()
        achou = False

        for h in horarios:
            if h.get_id_cliente() == st.session_state["usuario_id"]:
                achou = True
                profissional = View.profissional_listar_id(h.get_id_profissional())
                servico = View.servico_listar_id(h.get_id_servico())

                st.write(f"📅 {h.get_data().strftime('%d/%m/%Y %H:%M')}")
                st.write(f"👨‍🔧 Profissional: {profissional.get_nome()}")
                st.write(f"💈 Serviço: {servico.get_descricao()}")
                st.write(f"✅ Confirmado: {'Sim' if h.get_confirmado() else 'Não'}")
                st.markdown("---")

        if not achou:
            st.info("Você ainda não possui serviços agendados.")