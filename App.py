import streamlit as st
import pandas as pd
import plotly.express as px
from modules.Conexao import conn  # <--- conexão vem daqui

st.set_page_config(
    page_title="Análise",
    page_icon="assets/Logo.png",
    layout="wide"
)

st.markdown("""
<style>
h1 {
    color: #ff9800;
}
</style>
""", unsafe_allow_html=True)
st.title("Painel de Gerenciamento de estabelecimento")
st.markdown("Análise Cupons Usados no estabelicento")

# Teste da conexão
if conn:
    st.success("Conexão com o banco estabelecida com sucesso!")
else:
    st.error("Falha na conexão com o banco de dados.")
