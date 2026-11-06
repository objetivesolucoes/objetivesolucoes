import streamlit as st

st.set_page_config(page_title="Diagnóstico Comercial", page_icon="📊")

st.title("📊 Diagnóstico de Eficiência Comercial")
st.subheader("Bem-vindo ao sistema de análise da Objetive Soluções")

st.write("Use este sistema para analisar os indicadores comerciais da sua empresa.")

# Exemplo de interação simples
nome_empresa = st.text_input("Digite o nome da sua empresa:")
if nome_empresa:
    st.success(f"Análise iniciada para: {nome_empresa}")
