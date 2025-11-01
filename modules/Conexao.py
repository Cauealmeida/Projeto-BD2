import streamlit as st
import psycopg2
import os
from dotenv import load_dotenv

# Caminho absoluto para o .env
env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '.env'))
print(f"🔍 Carregando .env de: {env_path}")

# Carrega o .env explicitamente
load_dotenv(dotenv_path=env_path)

# Debug: imprime as variáveis para conferir
print("DB_HOST:", os.getenv("DB_HOST"))
print("DB_NAME:", os.getenv("DB_NAME"))
print("DB_USER:", os.getenv("DB_USER"))
print("DB_PASSWORD:", os.getenv("DB_PASSWORD"))
print("DB_PORT:", os.getenv("DB_PORT"))

@st.cache_resource
def init_connection():
    try:
        conn = psycopg2.connect(
            host=os.getenv('DB_HOST'),
            database=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            port=os.getenv('DB_PORT')
        )
        print("✅ Conexão bem-sucedida com:", os.getenv('DB_HOST'))
        return conn
    except Exception as e:
        st.error(f"Erro na conexão: {e}")
        print("❌ Erro detalhado:", e)
        return None

conn = init_connection()
