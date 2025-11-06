import streamlit as st
from views import View

class VisualizarMinhaAgendaUI:
    def main():
        st.header("Minha Agenda de Atendimento")

        if "usuario_id" not in st.session_state or st.session_state.get("usuario_tipo") != "profissional":
            st.info("Acesse como profissional para ver sua agenda.")
            return

        prof_id = st.session_state["usuario_id"]
        horarios = View.horario_listar()  
        meus = [h for h in horarios if h.get_id_profissional() == prof_id]

        if len(meus) == 0:
            st.info("Nenhum horário cadastrado para você.")
            return

        for h in meus:
            data_str = h.get_data().strftime("%d/%m/%Y %H:%M")
            cliente = None
            servico = None
            if h.get_id_cliente():
                cliente = View.cliente_listar_id(h.get_id_cliente())
            if h.get_id_servico():
                servico = View.servico_listar_id(h.get_id_servico())

            st.markdown(f"**{data_str}**")
            st.write("Cliente:", cliente.get_nome() if cliente else "Disponível")
            st.write("Serviço:", servico.get_descricao() if servico else "-")
            st.write("Confirmado:", "Sim" if h.get_confirmado() else "Não")
            st.markdown("---")
