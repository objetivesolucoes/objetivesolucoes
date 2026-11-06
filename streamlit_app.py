import streamlit as st
import streamlit.components.v1 as components

# Configuração da página do Streamlit
st.set_page_config(
    page_title="Diagnóstico de Eficiência Comercial | Objetive",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Estilização para remover as margens padrões do Streamlit e preencher a tela inteira
st.markdown("""
    <style>
        .block-container { padding: 0px !important; }
        footer { visibility: hidden; }
        #MainMenu { visibility: hidden; }
        header { visibility: hidden; }
    </style>
""", unsafe_allow_html=True)

# Lendo o arquivo HTML separado de forma limpa e segura
try:
    with open("diagnostico.html", "r", encoding="utf-8") as f:
        html_code = f.read()
    
    # Renderiza o diagnóstico na tela ocupando a largura total e altura dinâmica
    components.html(html_code, height=2200, scrolling=True)
except Exception as e:
    st.error(f"Erro ao carregar o arquivo de diagnóstico: {e}")
