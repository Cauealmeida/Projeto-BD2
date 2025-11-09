import base64
import streamlit as st
import pandas as pd
import plotly.express as px
from modules.Conexao import conn

#configuração inicial do site
st.set_page_config(
    page_title="Análise",
    page_icon="assets/Logo.png",
    layout="wide"
)


#função para executar querys;
@st.cache_data(ttl=3600)
def run_query(query, params = None):
    try:
        df = pd.read_sql (query, conn, params= params)
        return df
    except Exception as e:
        st.error(f"Erro na query: {e}")
        return pd.DataFrame()


#Convertendo para base64 para o streamlit reconhecer.
def get_base64_image(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Caminho relativo da sua imagem
image_logo = get_base64_image("assets/Logo.png")
image_usuario = get_base64_image("assets/Usuario.png")

#criando o header
containerHeader = st.container(horizontal= True, horizontal_alignment="left",gap="small")
#cria o visual do header e estiliza
containerHeader.markdown(f"""
<style>
.header-container {{
    display: flex;
    align-items: center;
    border-bottom: 3px solid #ff9800;
    padding: 10px 0;
    justify-content: space-between;
}}
.header-logo {{
    width: 50px;
    margin-right: 15px;
}}
.header-text {{
    color: #ff9800;
    font-family: 'Segoe UI', sans-serif;
    font-size: 1.5rem;
    margin: 0;
    padding: 0;
}}
.ancora {{
    text-decoration: none !important;
    color: #ff9800 !important;
}}
.ancora:hover {{
    text-decoration: none !important;
    color: #ffa726 !important;
    font-size: 15px;
}}
.ancora img {{
    margin-left: 10px;
    width: 55px;
    border-radius: 50%;
}}
</style>

<div class="header-container">
    <div style="display: flex; align-items: center;">
        <img class="header-logo" src="data:image/png;base64,{image_logo}">
        <h4 class="header-text">Painel de Gerenciamento de Informações do Estabelecimento</h4>
    </div>
    <a href="#" class="ancora">
        Padaria Pão de Sucesso 11.656.490/0001-04
        <img src="data:image/png;base64,{image_usuario}">
    </a>
</div>
""", unsafe_allow_html=True)

#criando o body.
containerBody = st.container(border=True)

#criando as abas que contem os relatórios.
tab1, tab2, tab3 = containerBody.tabs(["Grafico1", "Grafico2", "Grafico3"])

with tab1:
    st.write("teste1")

with tab2:
    st.write("teste2")

with tab3:
    st.write("teste3")







# Teste da conexão
#if conn:
    #st.success("Conexão com o banco estabelecida com sucesso!")
#else:
    #st.error("Falha na conexão com o banco de dados.")
