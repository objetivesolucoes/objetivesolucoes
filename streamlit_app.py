import streamlit as st

st.set_page_config(page_title="Diagnóstico Comercial", page_icon="📊", layout="centered")

# Controla em qual tela o usuário está (Estado da Sessão)
if "passo" not in st.session_state:
    st.session_state.passo = 1
if "dados" not in st.session_state:
    st.session_state.dados = {}

# --- TELA 1: IDENTIFICAÇÃO ---
if st.session_state.passo == 1:
    st.title("📊 Diagnóstico de Eficiência Comercial")
    st.write("Bem-vindo! Vamos analisar a maturidade comercial da sua empresa.")
    
    nome = st.text_input("Nome da Empresa:", value=st.session_state.dados.get("nome", ""))
    setor = st.selectbox("Setor de Atuação:", ["Tecnologia", "Serviços", "Varejo/Comércio", "Indústria", "Outro"])
    
    st.write("")
    if st.button("Iniciar Diagnóstico ➡️"):
        if nome:
            st.session_state.dados["nome"] = nome
            st.session_state.dados["setor"] = setor
            st.session_state.passo = 2
            st.rerun()
        else:
            st.warning("Por favor, preencha o nome da empresa para continuar.")

# --- TELA 2: PERGUNTAS DO DIAGNÓSTICO ---
elif st.session_state.passo == 2:
    st.title("📝 Avaliação Comercial")
    st.write(f"Empresa: **{st.session_state.dados['nome']}** | Setor: {st.session_state.dados['setor']}")
    st.markdown("---")
    
    st.subheader("Pergunta 1: Como é feita a captação de clientes atualmente?")
    p1 = st.radio("Selecione uma opção:", [
        "Não temos processo definido (Indicação/Passivo)",
        "Processo manual e pouco previsível",
        "Processo estruturado com ferramentas e metas claras"
    ])
    
    st.subheader("Pergunta 2: A sua empresa utiliza um sistema de CRM?")
    p2 = st.radio("Selecione uma opção:", [
        "Não usamos nenhum sistema",
        "Usamos planilhas de Excel/Sheets",
        "Sim, usamos um CRM de mercado ativamente"
    ])

    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Voltar"):
            st.session_state.passo = 1
            st.rerun()
    with col2:
        if st.button("Ver Resultado Final 📊"):
            st.session_state.dados["p1"] = p1
            st.session_state.dados["p2"] = p2
            st.session_state.passo = 3
            st.rerun()

# --- TELA 3: RESULTADO FINAL ---
elif st.session_state.passo == 3:
    st.title("🏁 Resultado do seu Diagnóstico")
    st.write(f"Obrigado por responder, **{st.session_state.dados['nome']}**!")
    st.markdown("---")
    
    # Lógica simples para gerar uma nota baseada nas respostas
    pontos = 0
    if "estruturado" in st.session_state.dados["p1"]: pontos += 50
    elif "manual" in st.session_state.dados["p1"]: pontos += 25
        
    if "CRM de mercado" in st.session_state.dados["p2"]: pontos += 50
    elif "planilhas" in st.session_state.dados["p2"]: pontos += 25
    
    st.metric(label="Sua Nota de Eficiência Comercial", value=f"{pontos} / 100")
    
    if pontos <= 25:
        st.error("🚨 **Nível Inicial:** Sua operação comercial precisa de estruturação urgente. Você está muito dependente de indicações.")
    elif pontos <= 75:
        st.warning("⚠️ **Nível Intermediário:** Você já tem controles básicos, mas falta automação e previsibilidade para crescer com segurança.")
    else:
        st.success("✅ **Nível Avançado:** Parabéns! Sua empresa possui processos modernos e ferramentas ideais de escala.")
        
    st.markdown("---")
    if st.button("🔄 Refazer Diagnóstico"):
        st.session_state.passo = 1
        st.session_state.dados = {}
        st.rerun()
