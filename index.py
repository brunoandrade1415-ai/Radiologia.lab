import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="RadioLab - Edição Bruno Andrade",
    page_icon="🦴",
    layout="wide"
)

# Estilização com fontes maiores, tema neon e visual descontraído
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    .stApp {
        background-color: #0d1117;
        color: #f0f6fc;
    }
    
    /* Fontes e Títulos Maiores */
    h1 {
        font-size: 2.6rem !important;
        font-weight: 800 !important;
        color: #58a6ff !important;
    }
    h2 {
        font-size: 1.8rem !important;
        color: #7ee787 !important;
    }
    h3 {
        font-size: 1.4rem !important;
        color: #ffa657 !important;
    }
    
    /* Card de Memorando / Homenagem */
    .memo-card {
        background: linear-gradient(135deg, #1f242d 0%, #161b22 100%);
        border: 2px solid #388bfd;
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 25px;
        box-shadow: 0px 4px 15px rgba(56, 139, 253, 0.2);
    }
    
    /* Abas Estilizadas */
    .stTabs [data-baseweb="tab-list"] {
        gap: 12px;
        background-color: #161b22;
        padding: 12px;
        border-radius: 14px;
        border: 1px solid #30363d;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: #21262d;
        color: #c9d1d9 !important;
        border-radius: 10px;
        padding: 12px 22px;
        font-size: 17px;
        font-weight: 700;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #238636 !important;
        color: #ffffff !important;
        border: 1px solid #3fb950 !important;
        box-shadow: 0px 0px 12px rgba(63, 185, 80, 0.6);
    }
    
    /* Cards de Conteúdo */
    .content-box {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 14px;
        padding: 18px;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# HOMENAGEM & MEMORANDO DE CO-CRIAÇÃO
st.markdown("""
<div class="memo-card">
    <span style="background-color: #388bfd; color: #fff; padding: 4px 12px; border-radius: 20px; font-weight: bold; font-size: 0.85rem;">
        🚀 CRÉDITOS DE CO-CRIAÇÃO
    </span>
    <h2 style="margin-top: 10px; margin-bottom: 5px; color: #ffffff !important;">Plataforma RadioLab - Guia Interativo de Radiologia</h2>
    <p style="font-size: 1.15rem; color: #8b949e; margin-bottom: 0px;">
        Idealizado e construído por <strong>Bruno Andrade</strong> em colaboração com o assistente IA. Um ambiente dinâmico, visual e moderno focado em simplificar o estudo radiológico sem enrolação!
    </p>
</div>
""", unsafe_allow_html=True)

# Navegação por Abas
tab_patologias, tab_calc, tab_quiz, tab_socorros, tab_galeria = st.tabs([
    "🦴 1. Fraturas & Bizus Visual", 
    "⚡ 2. Raio-X Tech (kV/mAs)", 
    "🎯 3. Game Quiz Rad", 
    "🚑 4. Quiz Socorros", 
    "🖼️ 5. Galeria de Exames"
])

# ABA 1: FRATURAS, ANATÔMICOS E BIZUS VISUAL
with tab_patologias:
    st.header("🦴 Guia Visual: Fraturas, Lesões & Bizus")
    st.write("Conecte a anatomia com as imagens e pegue o traço radiolúcido sem vacilar!")
    
    col_img1, col_img2 = st.columns(2)
    
    with col_img1:
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        st.subheader("📍 Fratura de Escafóide (Punho)")
        st.image("https://upload.wikimedia.org/wikipedia/commons/8/87/Scaphoid_fracture.jpg", use_container_width=True)
        st.write("**Bizu de Ouro:** Fique atento à 'cintura do escafóide'. Às vezes a fratura só aparece na incidência específica para Escafóide com desvio ulnar!")
        st.markdown('</div>', unsafe_allow_html=True)

    with col_img2:
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        st.subheader("📍 Fratura de Rádio Distal (Colles)")
        st.image("https://upload.wikimedia.org/wikipedia/commons/2/23/Colles_fracture_AP_and_lateral.jpg", use_container_width=True)
        st.write("**Bizu de Ouro:** O clássico desvio dorsal com aspecto de 'garfo de mesa'. Repare na descontinuidade da cortical óssea.")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("💡 Bizus Rápidos de Posicionamento")
    
    b1, b2 = st.columns(2)
    with b1:
        st.info("🫁 **Tórax PA:** Abra o peito e rode os ombros pra frente (mão no quadril) pra varrer a escápula para fora do pulmão!")
    with b2:
        st.success("🖐️ **Mão Perfil:** Posição em 'leque' com os dedos separados pra não virar uma bagunça de metacarpais sobrepostos.")

# ABA 2: CALCULADORA DE TÉCNICA (KV / MAS)
with tab_calc:
    st.header("⚡ Raio-X Tech: Calculadora de KV e mAs")
    st.write("Sem adivinhação! Ajuste os sliders de acordo com o paciente e pegue a dose certa.")

    col_input, col_result = st.columns([1, 1])
    
    with col_input:
        st.subheader("⚙️ Parâmetros do Exame")
        espessura = st.slider("Espessura da Estrutura (cm):", min_value=1, max_value=50, value=15, step=1)
        constante = st.number_input("Constante do Aparelho (C):", min_value=20, max_value=50, value=30)
        fator_mAs = st.radio("Região Anatômica:", ["Membros / Dedos (0.10)", "Tórax / Abdômen (0.15)", "Bacia / Coluna (0.20)"], index=1)

    with col_result:
        st.subheader("📊 Disparo Sugerido")
        
        mult = 0.15
        if "0.10" in fator_mAs: mult = 0.10
        elif "0.20" in fator_mAs: mult = 0.20
        
        kv_calculado = (espessura * 2) + constante
        mas_calculado = kv_calculado * mult

        st.metric(label="⚡ Quilovoltagem (kV)", value=f"{kv_calculado:.0f} kV")
        st.metric(label="💥 Miliamperagem x Tempo (mAs)", value=f"{mas_calculado:.1f} mAs")
        
        st.progress(min(int(kv_calculado), 100) / 100)

# ABA 3: GAME QUIZ RAD (1 PERGUNTA POR TELA)
with tab_quiz:
    st.header("🎯 Game Quiz Rad")
    st.write("Testando sua visão de raio-x! Responda uma pergunta por vez.")

    questions = [
        {
            "pergunta": "1. Por que rodamos os ombros para a frente na incidência de Tórax em PA?",
            "opcoes": [
                "Para aproximar o coração da estativa",
                "Para afastar as escápulas dos campos pulmonares",
                "Para diminuir o tempo de exposição",
                "Para alinhar as clavículas na vertical"
            ],
            "correta": "Para afastar as escápulas dos campos pulmonares",
            "explicacao": "Boa! Rodar os ombros desloca as escápulas lateralmente, deixando os campos pulmonares livres de sombras."
        },
        {
            "pergunta": "2. Como se chama a linha escura que indica a ruptura da cortical óssea em uma radiografia?",
            "opcoes": [
                "Traço de Esclerose",
                "Linha de Sutura Anatômica",
                "Linha Radiolúcida de Fratura",
                "Artefato de Grade"
            ],
            "correta": "Linha Radiolúcida de Fratura",
            "explicacao": "Na mosca! A ruptura do osso deixa passar mais radiação, formando o traço radiolúcido (mais escuro)."
        },
        {
            "pergunta": "3. Para examinar o osso Escafóide no punho, qual desvio é aplicado na mão do paciente?",
            "opcoes": [
                "Desvio Ulnar",
                "Desvio Radial",
                "Flexão Palmar Extrema",
                "Prono-supinação Média"
            ],
            "correta": "Desvio Ulnar",
            "explicacao": "Perfeito! O desvio ulnar abre o espaço articular e alinha o eito do escafóide paralelo ao filme."
        }
    ]

    if "q_index" not in st.session_state:
        st.session_state.q_index = 0
    if "score" not in st.session_state:
        st.session_state.score = 0

    idx = st.session_state.q_index

    if idx < len(questions):
        q = questions[idx]
        st.progress((idx + 1) / len(questions))
        st.subheader(q["pergunta"])

        resposta = st.radio("Escolha uma opção:", q["opcoes"], key=f"q_rad_{idx}")

        if st.button("Responder e Avançar 🚀"):
            if resposta == q["correta"]:
                st.session_state.score += 10
                st.success(f"Mandou ver! {q['explicacao']}")
            else:
                st.error(f"Ops! A resposta certa era: {q['correta']}")
            
            st.session_state.q_index += 1
            st.rerun()

    else:
        st.balloons()
        st.success(f"🏆 Quiz Concluído! Você somou {st.session_state.score} pontos.")
        if st.button("Reiniciar Game Quiz 🔄"):
            st.session_state.q_index = 0
            st.session_state.score = 0
            st.rerun()

# ABA 4: QUIZ PRIMEIROS SOCORROS (1 PERGUNTA POR TELA)
with tab_socorros:
    st.header("🚑 Quiz de Primeiros Socorros na Radiologia")
    st.write("Saber agir rápido na sala de exames salva vidas!")

    socorro_questions = [
        {
            "pergunta": "1. O paciente teve uma crise convulsiva na mesa de exames. O que você NÃO deve fazer?",
            "opcoes": [
                "Proteger a cabeça do paciente",
                "Afastar objetos cortantes ao redor",
                "Colocar a mão ou colher na boca dele para segurar a língua",
                "Vira-lo de lado após o término da crise"
            ],
            "correta": "Colocar a mão ou colher na boca dele para segurar a língua",
            "explicacao": "Exatamente! Nunca coloque nada na boca de alguém em crise convulsiva. Apenas proteja a cabeça e afaste objetos!"
        },
        {
            "pergunta": "2. Durante a aplicação de contraste iodado, o paciente relata falta de ar e coceira intensa. Qual é a suspeita?",
            "opcoes": [
                "Lipotimia por ansiedade",
                "Reação de Choque Anafilático",
                "Hipoglicemia leve",
                "Efeito colateral normal e sem gravidade"
            ],
            "correta": "Reação de Choque Anafilático",
            "explicacao": "Certo! Sintomas respiratórios e cutâneos intensos exigem interrupção imediata do contraste e acionamento da emergência!"
        },
        {
            "pergunta": "3. Paciente ficou tonto ao se levantar do Bucky vertical ('visão preta'). Qual a conduta inicial?",
            "opcoes": [
                "Oferecer um copo de água fervendo",
                "Sentar ou deitar o paciente imediatamente para evitar queda",
                "Pedir para ele caminhar rápido para ativar a circulação",
                "Continuar o exame rapidamente"
            ],
            "correta": "Sentar ou deitar o paciente imediatamente para evitar queda",
            "explicacao": "Boa! Isso é pré-síncope/lipotimia. Sentar ou deitar evita trauma por queda súbita."
        }
    ]

    if "soc_index" not in st.session_state:
        st.session_state.soc_index = 0
    if "soc_score" not in st.session_state:
        st.session_state.soc_score = 0

    s_idx = st.session_state.soc_index

    if s_idx < len(socorro_questions):
        sq = socorro_questions[s_idx]
        st.progress((s_idx + 1) / len(socorro_questions))
        st.subheader(sq["pergunta"])

        s_resposta = st.radio("Escolha a conduta correta:", sq["opcoes"], key=f"q_soc_{s_idx}")

        if st.button("Confirmar Ação 🚑"):
            if s_resposta == sq["correta"]:
                st.session_state.soc_score += 10
                st.success(f"Excelente conduta! {sq['explicacao']}")
            else:
                st.error(f"Atenção! A conduta correta era: {sq['correta']}")
            
            st.session_state.soc_index += 1
            st.rerun()

    else:
        st.balloons()
        st.success(f"🎉 Módulo de Socorros Finalizado! Pontuação: {st.session_state.soc_score} pontos.")
        if st.button("Refazer Quiz Socorros 🔄"):
            st.session_state.soc_index = 0
            st.session_state.soc_score = 0
            st.rerun()

# ABA 5: GALERIA DE EXAMES
with tab_galeria:
    st.header("🖼️ Galeria Visual de Referência")
    st.write("Acervo de exames radiográficos para consulta rápida.")

    casos = [
        {
            "titulo": "Luxação Acromioclavicular",
            "desc": "Perda do alinhamento entre a clavícula distal e o acrômio.",
            "url": "https://upload.wikimedia.org/wikipedia/commons/8/87/Acromioclavicular_dislocation_xray.jpg"
        },
        {
            "titulo": "Fratura Cominutiva de Fêmur",
            "desc": "Múltiplos fragmentos ósseos por trauma de alta energia.",
            "url": "https://upload.wikimedia.org/wikipedia/commons/4/4b/Comminuted_femur_fracture.jpg"
        }
    ]

    g1, g2 = st.columns(2)
    with g1:
        st.subheader(casos[0]["titulo"])
        st.image(casos[0]["url"], use_container_width=True)
        st.caption(casos[0]["desc"])

    with g2:
        st.subheader(casos[1]["titulo"])
        st.image(casos[1]["url"], use_container_width=True)
        st.caption(casos[1]["desc"])
