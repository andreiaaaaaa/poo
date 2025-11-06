import streamlit as st
from views import View

class VisualizarMeusServicosUI:
    def main():
        st.header("Meus Serviços Agendados")

        if "usuario_id" not in st.session_state or st.session_state.get("usuario_tipo") != "cliente":
            st.info("Acesse como cliente para ver seus serviços.")
            return

        cli_id = st.session_state["usuario_id"]
        horarios = View.horario_listar()

        meus = [h for h in horarios if h.get_id_cliente() == cli_id]

        if len(meus) == 0:
            st.info("Você não tem serviços agendados.")
            return

        for h in meus:
            data_str = h.get_data().strftime("%d/%m/%Y %H:%M")
            prof = View.profissional_listar_id(h.get_id_profissional()) if h.get_id_profissional() else None
            serv = View.servico_listar_id(h.get_id_servico()) if h.get_id_servico() else None

            st.markdown(f"**{data_str}**")
            st.write("Profissional:", prof.get_nome() if prof else "-")
            st.write("Serviço:", serv.get_descricao() if serv else "-")
            st.write("Confirmado:", "Sim" if h.get_confirmado() else "Não")
            st.markdown("---")
