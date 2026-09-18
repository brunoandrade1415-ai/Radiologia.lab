import streamlit as st

# Configuração da página
st.set_page_config(page_title="RadioLingo", page_icon="🦴", layout="wide")

st.title("🦴 RadioLingo - Aprendizado Gamificado de Radiologia")
st.write("Escolha um módulo nas abas abaixo para praticar seus conhecimentos com o estilo Duolingo!")

# -----------------------------------------------------------------------------
# FUNÇÃO REUTILIZÁVEL PARA RENDERIZAR O QUIZ EM HTML/JS
# -----------------------------------------------------------------------------
def render_quiz(quiz_id, questions_json):
    html_code = f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <style>
            :root {{
                --green: #58cc02;
                --green-dark: #46a302;
                --red: #ff4b4b;
                --red-dark: #ea2b2b;
                --blue: #1cb0f6;
                --gray: #e5e5e5;
                --text: #3c3c3c;
            }}
            * {{
                box-sizing: border-box;
                font-family: 'Nunito', sans-serif, system-ui;
                margin: 0;
                padding: 0;
            }}
            body {{
                background-color: #f7f7f7;
                color: var(--text);
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 10px;
            }}
            .quiz-container {{
                width: 100%;
                max-width: 650px;
                background: white;
                border-radius: 16px;
                border: 2px solid var(--gray);
                padding: 20px;
                box-shadow: 0 4px 0 var(--gray);
            }}
            .top-bar {{
                display: flex;
                align-items: center;
                gap: 16px;
                margin-bottom: 20px;
            }}
            .progress-bar-bg {{
                flex-grow: 1;
                height: 16px;
                background-color: var(--gray);
                border-radius: 8px;
                overflow: hidden;
            }}
            .progress-bar-fill {{
                height: 100%;
                width: 0%;
                background-color: var(--green);
                transition: width 0.3s ease;
            }}
            .stats {{
                display: flex;
                gap: 12px;
                font-weight: bold;
                font-size: 1.1rem;
            }}
            .question-title {{
                font-size: 1.2rem;
                margin-bottom: 16px;
            }}
            .illustration-box {{
                width: 100%;
                height: 160px;
                background: #f0f4f8;
                border-radius: 12px;
                display: flex;
                justify-content: center;
                align-items: center;
                margin-bottom: 20px;
                border: 2px dashed #b0c4de;
            }}
            .illustration-box svg {{
                max-height: 130px;
            }}
            .options-grid {{
                display: grid;
                gap: 10px;
                margin-bottom: 20px;
            }}
            .option-btn {{
                background: white;
                border: 2px solid var(--gray);
                border-bottom-width: 4px;
                border-radius: 12px;
                padding: 12px 16px;
                font-size: 1rem;
                font-weight: 600;
                color: var(--text);
                cursor: pointer;
                text-align: left;
            }}
            .option-btn:hover {{ background-color: #f7f7f7; }}
            .option-btn.selected {{
                border-color: var(--blue);
                background-color: #ddf4ff;
                color: #0077b6;
            }}
            .action-btn {{
                width: 100%;
                background-color: var(--green);
                color: white;
                border: none;
                border-bottom: 4px solid var(--green-dark);
                border-radius: 12px;
                padding: 14px;
                font-size: 1.1rem;
                font-weight: bold;
                cursor: pointer;
                text-transform: uppercase;
            }}
            .feedback-panel {{
                margin-top: 16px;
                padding: 14px;
                border-radius: 12px;
                display: none;
            }}
            .feedback-panel.correct {{ display: block; background-color: #d7ffb8; color: #2b6100; }}
            .feedback-panel.incorrect {{ display: block; background-color: #ffdfe0; color: var(--red-dark); }}
            .feedback-title {{ font-weight: bold; font-size: 1.1rem; margin-bottom: 4px; }}
        </style>
    </head>
    <body>
    <div class="quiz-container">
        <div class="top-bar">
            <div class="progress-bar-bg"><div class="progress-bar-fill" id="progress_{quiz_id}"></div></div>
            <div class="stats">
                <div style="color: var(--red);">❤️ <span id="lives_{quiz_id}">3</span></div>
                <div style="color: #ff9600;">⚡ <span id="xp_{quiz_id}">0</span></div>
            </div>
        </div>

        <div id="quiz-body_{quiz_id}">
            <h2 class="question-title" id="question-text_{quiz_id}">Carregando...</h2>
            <div class="illustration-box" id="illustration-container_{quiz_id}"></div>
            <div class="options-grid" id="options-container_{quiz_id}"></div>
            <button class="action-btn" id="check-btn_{quiz_id}" onclick="checkAnswer_{quiz_id}()">Verificar</button>
            <div class="feedback-panel" id="feedback_{quiz_id}">
                <div class="feedback-title" id="feedback-title_{quiz_id}"></div>
                <div id="feedback-text_{quiz_id}"></div>
            </div>
        </div>
    </div>

    <script>
        const questions_{quiz_id} = {questions_json};
        let currentIdx_{quiz_id} = 0;
        let selectedOption_{quiz_id} = null;
        let lives_{quiz_id} = 3;
        let xp_{quiz_id} = 0;
        let isChecked_{quiz_id} = false;

        function loadQuestion_{quiz_id}() {{
            isChecked_{quiz_id} = false;
            selectedOption_{quiz_id} = null;
            const q = questions_{quiz_id}[currentIdx_{quiz_id}];

            document.getElementById("question-text_{quiz_id}").innerText = q.question;
            document.getElementById("illustration-container_{quiz_id}").innerHTML = q.svg;
            
            const optionsGrid = document.getElementById("options-container_{quiz_id}");
            optionsGrid.innerHTML = "";

            q.options.forEach((opt, idx) => {{
                const btn = document.createElement("button");
                btn.className = "option-btn";
                btn.innerText = opt;
                btn.onclick = () => selectOption_{quiz_id}(idx, btn);
                optionsGrid.appendChild(btn);
            }});

            document.getElementById("feedback_{quiz_id}").style.display = "none";
            document.getElementById("check-btn_{quiz_id}").innerText = "Verificar";
            
            const progressPct = ((currentIdx_{quiz_id}) / questions_{quiz_id}.length) * 100;
            document.getElementById("progress_{quiz_id}").style.width = `${{progressPct}}%`;
        }}

        function selectOption_{quiz_id}(idx, element) {{
            if (isChecked_{quiz_id}) return;
            document.querySelectorAll("#options-container_{quiz_id} .option-btn").forEach(btn => btn.classList.remove("selected"));
            element.classList.add("selected");
            selectedOption_{quiz_id} = idx;
        }}

        function checkAnswer_{quiz_id}() {{
            if (isChecked_{quiz_id}) {{
                currentIdx_{quiz_id}++;
                if (currentIdx_{quiz_id} < questions_{quiz_id}.length) {{
                    loadQuestion_{quiz_id}();
                }} else {{
                    alert(`Parabéns! Módulo concluído com ${{xp_{quiz_id}}} XP!`);
                    currentIdx_{quiz_id} = 0;
                    lives_{quiz_id} = 3;
                    xp_{quiz_id} = 0;
                    document.getElementById("lives_{quiz_id}").innerText = lives_{quiz_id};
                    document.getElementById("xp_{quiz_id}").innerText = xp_{quiz_id};
                    loadQuestion_{quiz_id}();
                }}
                return;
            }}

            if (selectedOption_{quiz_id} === null) return;

            isChecked_{quiz_id} = true;
            const q = questions_{quiz_id}[currentIdx_{quiz_id}];
            const feedbackEl = document.getElementById("feedback_{quiz_id}");
            const feedbackTitle = document.getElementById("feedback-title_{quiz_id}");
            const feedbackText = document.getElementById("feedback-text_{quiz_id}");

            if (selectedOption_{quiz_id} === q.answer) {{
                feedbackEl.className = "feedback-panel correct";
                feedbackTitle.innerText = "Excelente!";
                feedbackText.innerText = q.explanation;
                xp_{quiz_id} += 10;
                document.getElementById("xp_{quiz_id}").innerText = xp_{quiz_id};
            }} else {{
                feedbackEl.className = "feedback-panel incorrect";
                feedbackTitle.innerText = "Resposta correta:";
                feedbackText.innerText = `${{q.options[q.answer]}} - ${{q.explanation}}`;
                lives_{quiz_id}--;
                document.getElementById("lives_{quiz_id}").innerText = lives_{quiz_id};

                if (lives_{quiz_id} <= 0) {{
                    alert("Suas vidas acabaram! Reiniciando a lição.");
                    currentIdx_{quiz_id} = 0;
                    lives_{quiz_id} = 3;
                    xp_{quiz_id} = 0;
                    document.getElementById("lives_{quiz_id}").innerText = lives_{quiz_id};
                    document.getElementById("xp_{quiz_id}").innerText = xp_{quiz_id};
                    loadQuestion_{quiz_id}();
                    return;
                }}
            }}

            feedbackEl.style.display = "block";
            document.getElementById("check-btn_{quiz_id}").innerText = "Continuar";
        }}

        loadQuestion_{quiz_id}();
    </script>
    </body>
    </html>
    """
    st.components.v1.html(html_code, height=620, scrolling=True)


# -----------------------------------------------------------------------------
# BANCOS DE QUESTÕES POR MÓDULO
# -----------------------------------------------------------------------------

# MÓDULO 1: OSTEOLOGIA
m1_questions = [
    {
        "id": 1,
        "question": "Qual estrutura vascularizada reveste a superfície externa dos ossos?",
        "svg": '<svg viewBox="0 0 200 100" width="180"><rect x="20" y="35" width="160" height="30" rx="10" fill="#e0e0e0" stroke="#333" stroke-width="2"/><rect x="20" y="35" width="160" height="5" fill="#ff4b4b"/><rect x="20" y="60" width="160" height="5" fill="#ff4b4b"/><text x="100" y="53" font-size="10" text-anchor="middle" fill="#333">Periósteo Externo</text></svg>',
        "options": ["Epífise", "Canal Medular", "Periósteo", "Cartilagem Articular"],
        "answer": 2,
        "explanation": "O periósteo reveste a diáfise e é vital para a nutrição e regeneração do osso."
    },
    {
        "id": 2,
        "question": "O esqueleto apendicular humano é composto por quantos ossos no total?",
        "svg": '<svg viewBox="0 0 200 100" width="180"><circle cx="100" cy="50" r="35" fill="#ddf4ff" stroke="#1cb0f6" stroke-width="3"/><text x="100" y="55" font-size="18" font-weight="bold" text-anchor="middle" fill="#0077b6">126</text></svg>',
        "options": ["80 ossos", "206 ossos", "126 ossos", "64 ossos"],
        "answer": 2,
        "explanation": "O esqueleto apendicular possui 126 ossos (membros e cinturas). O axial possui 80, totalizando 206."
    }
]

# MÓDULO 2: COLUNA & TÓRAX
m2_questions = [
    {
        "id": 1,
        "question": "Quantas vértebras compõem a região torácica da coluna vertebral?",
        "svg": '<svg viewBox="0 0 200 100" width="180"><path d="M100,10 Q110,50 100,90" stroke="#ff9600" stroke-width="6" fill="none"/><text x="130" y="55" font-size="14" font-weight="bold" fill="#ff9600">T1-T12</text></svg>',
        "options": ["7 vértebras", "12 vértebras", "5 vértebras", "4 vértebras"],
        "answer": 1,
        "explanation": "A região torácica abriga 12 vértebras (T1 a T12), articulando-se com as 12 costelas."
    },
    {
        "id": 2,
        "question": "As costelas flutuantes são representadas por quais pares?",
        "svg": '<svg viewBox="0 0 200 100" width="180"><path d="M50,30 Q100,10 150,30 M60,50 Q100,30 140,50 M70,70 Q100,60 130,70" stroke="#333" stroke-width="3" fill="none"/><text x="100" y="90" font-size="10" text-anchor="middle" fill="#ff4b4b">Costelas Flutuantes</text></svg>',
        "options": ["1º ao 7º par", "8º ao 10º par", "11º e 12º pares", "1º e 2º pares"],
        "answer": 2,
        "explanation": "Os pares 11 e 12 são flutuantes pois suas extremidades anteriores ficam livres."
    }
]

# MÓDULO 3: MEMBROS SUPERIORES (MMSS)
m3_questions = [
    {
        "id": 1,
        "question": "Na incidência em PA de Mão, onde deve incidir o Raio Central (RC)?",
        "svg": '<svg viewBox="0 0 200 100" width="180"><path d="M70,80 Q70,40 100,40 Q130,40 130,80 Z" fill="#ccc" stroke="#333" stroke-width="2"/><line x1="100" y1="10" x2="100" y2="50" stroke="#ff0000" stroke-width="3" stroke-dasharray="4"/><text x="100" y="95" font-size="9" text-anchor="middle">RC Perpendicular</text></svg>',
        "options": ["No carpo/punho", "Na cabeça do 3º metacarpo", "No osso escafóide", "Na falange distal"],
        "answer": 1,
        "explanation": "O RC incide perpendicularmente na 3ª articulação metacarpofalângica."
    },
    {
        "id": 2,
        "question": "Qual é o maior osso da fileira proximal do carpo, frequentemente fraturado em quedas?",
        "svg": '<svg viewBox="0 0 200 100" width="180"><ellipse cx="100" cy="50" rx="30" ry="20" fill="#58cc02" stroke="#3c3c3c" stroke-width="2"/><text x="100" y="54" font-size="10" font-weight="bold" text-anchor="middle" fill="#fff">Escafóide</text></svg>',
        "options": ["Semilunar", "Escafóide", "Piramidal", "Trapézio"],
        "answer": 1,
        "explanation": "O escafóide é o maior osso da fileira proximal e o mais susceptível a fraturas no punho."
    }
]

# MÓDULO 4: MEMBROS INFERIORES (MMII)
m4_questions = [
    {
        "id": 1,
        "question": "Qual a angulação do Raio Central para a incidência Axial de Calcâneo?",
        "svg": '<svg viewBox="0 0 200 100" width="180"><path d="M40,70 L140,70 L120,30 L60,30 Z" fill="#ddd" stroke="#333" stroke-width="2"/><line x1="130" y1="20" x2="80" y2="70" stroke="#ff0000" stroke-width="3"/><text x="135" y="30" font-size="10" fill="#ff0000" font-weight="bold">40° Cranial</text></svg>',
        "options": ["Perpendicular (0°)", "15° Caudal", "40° Cranial", "10° Cranial"],
        "answer": 2,
        "explanation": "A incidência exige 40° de angulação cranial direcionada para a base do 1º metatarso."
    },
    {
        "id": 2,
        "question": "Para a incidência em AP de Joelho, qual a posição padrão do paciente?",
        "svg": '<svg viewBox="0 0 200 100" width="180"><rect x="30" y="45" width="140" height="10" fill="#1cb0f6"/><circle cx="100" cy="50" r="15" fill="#ff9600"/><text x="100" y="85" font-size="10" text-anchor="middle">Decúbito Dorsal</text></svg>',
        "options": ["Decúbito Ventral com joelho fletido", "Decúbito Dorsal com perna estendida", "Ortostática em rotação externa", "Perfil absoluto"],
        "answer": 1,
        "explanation": "O paciente fica em decúbito dorsal com o membro estendido e a perna levemente rodada internamente (3° a 5°)."
    }
]

# -----------------------------------------------------------------------------
# INTERFACE COM ABAS NO STREAMLIT
# -----------------------------------------------------------------------------
tab1, tab2, tab3, tab4 = st.tabs([
    "🦴 1. Osteologia Geral", 
    "🫁 2. Coluna & Tórax", 
    "🖐️ 3. Membros Superiores", 
    "🦶 4. Membros Inferiores"
])

import json

with tab1:
    st.subheader("Módulo 1: Conceitos de Osteologia e Anatomia Básica")
    render_quiz("m1", json.dumps(m1_questions))

with tab2:
    st.subheader("Módulo 2: Coluna Vertebral e Caixa Torácica")
    render_quiz("m2", json.dumps(m2_questions))

with tab3:
    st.subheader("Módulo 3: Posicionamentos de MMSS")
    render_quiz("m3", json.dumps(m3_questions))

with tab4:
    st.subheader("Módulo 4: Posicionamentos de MMII")
    render_quiz("m4", json.dumps(m4_questions))
