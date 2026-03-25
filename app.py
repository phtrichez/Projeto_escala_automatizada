import streamlit as st
import pandas as pd

from src.scheduler import Scheduler
from src.trat1 import Tratamento1

st.set_page_config(page_title="Escala Automática", layout="centered")

st.title("📅 Gerador de Escala Automática")

file = st.file_uploader("Upload da escala", type=["csv", "xlsx"])

# =====================
# Carregar dados
# =====================
if file is not None:

    if "df" not in st.session_state:
        if file.name.endswith(".csv"):
            st.session_state.df = pd.read_csv(file)
        else:
            st.session_state.df = pd.read_excel(file)

        st.session_state.nomes = Tratamento1(st.session_state.df).nomes()

# =====================
# Mostrar filtro SEM botão
# =====================
if "nomes" in st.session_state:

    nomes = st.session_state.nomes

    st.subheader("Filtro de Nomes")

    selecionar_todos = st.checkbox("Selecionar todos", value=True)

    if selecionar_todos:
        nomes_selecionados = list(nomes)
    else:
        nomes_selecionados = st.multiselect(
            "Escolha os nomes",
            options=nomes,
            default=nomes
        )


    st.write("Selecionados:", nomes_selecionados)

    # =====================
    # Gerar escala
    # =====================
    if st.button("🚀 Gerar Escala"):

        scheduler = Scheduler(st.session_state.df, nomes_selecionados)
        df_result = scheduler.run()

        st.success("✅ Escala gerada com sucesso!")
        st.dataframe(df_result)

        from io import BytesIO

        output = BytesIO()

        df_result.to_excel(output, index=False, engine='openpyxl')

        st.download_button(
            label="📥 Baixar Excel",
            data=output.getvalue(),
            file_name="escala_final.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )