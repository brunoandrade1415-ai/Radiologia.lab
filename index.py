<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RadioLingo - Plataforma Interativa</title>
    <style>
        :root {
            --green: #58cc02;
            --green-dark: #46a302;
            --red: #ff4b4b;
            --red-dark: #ea2b2b;
            --blue: #1cb0f6;
            --gray: #e5e5e5;
            --text: #3c3c3c;
        }

        * {
            box-sizing: border-box;
            font-family: 'Din Round', 'Nunito', sans-serif, system-ui;
            margin: 0;
            padding: 0;
        }

        body {
            background-color: #f7f7f7;
            color: var(--text);
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }

        .quiz-container {
            width: 100%;
            max-width: 600px;
            background: white;
            border-radius: 16px;
            border: 2px solid var(--gray);
            padding: 24px;
            box-shadow: 0 4px 0 var(--gray);
        }

        /* Top Bar */
        .top-bar {
            display: flex;
            align-items: center;
            gap: 16px;
            margin-bottom: 24px;
        }

        .progress-bar-bg {
            flex-grow: 1;
            height: 16px;
            background-color: var(--gray);
            border-radius: 8px;
            overflow: hidden;
        }

        .progress-bar-fill {
            height: 100%;
            width: 0%;
            background-color: var(--green);
            transition: width 0.3s ease;
        }

        .stats {
            display: flex;
            gap: 12px;
            font-weight: bold;
        }

        .stat-item {
            display: flex;
            align-items: center;
            gap: 4px;
        }

        /* Question Section */
        .question-title {
            font-size: 1.25rem;
            margin-bottom: 16px;
        }

        .illustration-box {
            width: 100%;
            height: 180px;
            background: #f0f4f8;
            border-radius: 12px;
            display: flex;
            justify-content: center;
            align-items: center;
            margin-bottom: 20px;
            border: 2px dashed #b0c4de;
        }

        .illustration-box svg {
            max-height: 140px;
        }

        .options-grid {
            display: grid;
            gap: 12px;
            margin-bottom: 24px;
        }

        .option-btn {
            background: white;
            border: 2px solid var(--gray);
            border-bottom-width: 4px;
            border-radius: 12px;
            padding: 14px 18px;
            font-size: 1rem;
            font-weight: 600;
            color: var(--text);
            cursor: pointer;
            text-align: left;
            transition: all 0.1s ease;
        }

        .option-btn:hover {
            background-color: #f7f7f7;
        }

        .option-btn.selected {
            border-color: var(--blue);
            background-color: #ddf4ff;
            color: #0077b6;
        }

        /* Action / Footer */
        .action-btn {
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
        }

        .action-btn:active {
            transform: translateY(2px);
            border-bottom-width: 2px;
        }

        /* Feedback Panel */
        .feedback-panel {
            margin-top: 16px;
            padding: 16px;
            border-radius: 12px;
            display: none;
        }

        .feedback-panel.correct {
            display: block;
            background-color: #d7ffb8;
            color: #2b6100;
        }

        .feedback-panel.incorrect {
            display: block;
            background-color: #ffdfe0;
            color: var(--red-dark);
        }

        .feedback-title {
            font-weight: bold;
            font-size: 1.1rem;
            margin-bottom: 4px;
        }
    </style>
</head>
<body>

<div class="quiz-container">
    <!-- Barra Superior -->
    <div class="top-bar">
        <div class="progress-bar-bg">
            <div class="progress-bar-fill" id="progress"></div>
        </div>
        <div class="stats">
            <div class="stat-item" style="color: var(--red);">❤️ <span id="lives">3</span></div>
            <div class="stat-item" style="color: #ff9600;">⚡ <span id="xp">0</span></div>
        </div>
    </div>

    <!-- Conteúdo da Questão -->
    <div id="quiz-body">
        <h2 class="question-title" id="question-text">Carregando questão...</h2>
        
        <div class="illustration-box" id="illustration-container">
            <!-- Renderização do SVG Interativo -->
        </div>

        <div class="options-grid" id="options-container">
            <!-- Botões das opções via JS -->
        </div>

        <button class="action-btn" id="check-btn" onclick="checkAnswer()">Verificar</button>

        <div class="feedback-panel" id="feedback">
            <div class="feedback-title" id="feedback-title"></div>
            <div id="feedback-text"></div>
        </div>
    </div>
</div>

<script>
    // Banco de Dados de Questões (Extraído da nossa estrutura)
    const questions = [
        {
            id: 1,
            question: "Qual estrutura vascularizada reveste a superfície externa dos ossos?",
            svg: `<svg viewBox="0 0 200 100" width="180">
                    <rect x="20" y="35" width="160" height="30" rx="10" fill="#e0e0e0" stroke="#333" stroke-width="2"/>
                    <rect x="20" y="35" width="160" height="5" fill="#ff4b4b"/>
                    <rect x="20" y="60" width="160" height="5" fill="#ff4b4b"/>
                    <text x="100" y="53" font-size="10" text-anchor="middle" fill="#333">Diáfise + Membrana Red</text>
                  </svg>`,
            options: ["Epífise", "Canal Medular", "Periósteo", "Cartilagem Articular"],
            answer: 2,
            explanation: "O periósteo reveste a diáfise e é vital para a nutrição e regeneração do osso[span_0](start_span)[span_0](end_span)[span_1](start_span)[span_1](end_span)."
        },
        {
            id: 2,
            question: "Na incidência em PA de Mão, onde deve ser incidido o Raio Central (RC)?",
            svg: `<svg viewBox="0 0 200 100" width="180">
                    <path d="M70,80 Q70,40 100,40 Q130,40 130,80 Z" fill="#ccc" stroke="#333" stroke-width="2"/>
                    <line x1="100" y1="10" x2="100" y2="50" stroke="#ff0000" stroke-width="3" stroke-dasharray="4"/>
                    <polygon points="95,45 100,55 105,45" fill="#ff0000"/>
                    <text x="100" y="95" font-size="9" text-anchor="middle">Raio Central Perpendicular</text>
                  </svg>`,
            options: ["Na articulação do punho", "Na cabeça do 3º metacarpo", "No osso trapezoide", "Na falange distal"],
            answer: 1,
            explanation: "O Raio Central incide perpendicularmente na 3ª articulação metacarpofalângica[span_2](start_span)[span_2](end_span)."
        },
        {
            id: 3,
            question: "Qual a angulação do Raio Central para a incidência Axial de Calcâneo?",
            svg: `<svg viewBox="0 0 200 100" width="180">
                    <path d="M40,70 L140,70 L120,30 L60,30 Z" fill="#ddd" stroke="#333" stroke-width="2"/>
                    <line x1="130" y1="20" x2="80" y2="70" stroke="#ff0000" stroke-width="3"/>
                    <text x="135" y="30" font-size="10" fill="#ff0000" font-weight="bold">40° Cranial</text>
                  </svg>`,
            options: ["Perpendicular (0°)", "15° Caudal", "40° Cranial", "10° Cranial"],
            answer: 2,
            explanation: "A incidência exige 40° de angulação cranial em direção à base do primeiro metatarso[span_3](start_span)[span_3](end_span)."
        }
    ];

    let currentIdx = 0;
    let selectedOption = null;
    let lives = 3;
    let xp = 0;
    let isChecked = false;

    // Inicializar App
    function loadQuestion() {
        isChecked = false;
        selectedOption = null;
        const q = questions[currentIdx];

        document.getElementById("question-text").innerText = q.question;
        document.getElementById("illustration-container").innerHTML = q.svg;
        
        const optionsGrid = document.getElementById("options-container");
        optionsGrid.innerHTML = "";

        q.options.forEach((opt, idx) => {
            const btn = document.createElement("button");
            btn.className = "option-btn";
            btn.innerText = opt;
            btn.onclick = () => selectOption(idx, btn);
            optionsGrid.appendChild(btn);
        });

        // Reset UI
        document.getElementById("feedback").className = "feedback-panel";
        document.getElementById("feedback").style.display = "none";
        document.getElementById("check-btn").innerText = "Verificar";
        
        // Progresso
        const progressPct = ((currentIdx) / questions.length) * 100;
        document.getElementById("progress").style.width = `${progressPct}%`;
    }

    function selectOption(idx, element) {
        if (isChecked) return;
        
        document.querySelectorAll(".option-btn").forEach(btn => btn.classList.remove("selected"));
        element.classList.add("selected");
        selectedOption = idx;
    }

    function checkAnswer() {
        if (isChecked) {
            // Avançar para a próxima questão
            currentIdx++;
            if (currentIdx < questions.length) {
                loadQuestion();
            } else {
                alert(`Parabéns! Você concluiu a lição e ganhou ${xp} XP!`);
                currentIdx = 0;
                lives = 3;
                xp = 0;
                document.getElementById("lives").innerText = lives;
                document.getElementById("xp").innerText = xp;
                loadQuestion();
            }
            return;
        }

        if (selectedOption === null) return;

        isChecked = true;
        const q = questions[currentIdx];
        const feedbackEl = document.getElementById("feedback");
        const feedbackTitle = document.getElementById("feedback-title");
        const feedbackText = document.getElementById("feedback-text");

        if (selectedOption === q.answer) {
            // Resposta Correta
            feedbackEl.className = "feedback-panel correct";
            feedbackTitle.innerText = "Excelente!";
            feedbackText.innerText = q.explanation;
            xp += 10;
            document.getElementById("xp").innerText = xp;
        } else {
            // Resposta Incorreta
            feedbackEl.className = "feedback-panel incorrect";
            feedbackTitle.innerText = "Solução correta:";
            feedbackText.innerText = `${q.options[q.answer]} - ${q.explanation}`;
            lives--;
            document.getElementById("lives").innerText = lives;

            if (lives <= 0) {
                alert("Suas vidas acabaram! Reiniciando a lição.");
                currentIdx = 0;
                lives = 3;
                xp = 0;
                document.getElementById("lives").innerText = lives;
                document.getElementById("xp").innerText = xp;
                loadQuestion();
                return;
            }
        }

        feedbackEl.style.display = "block";
        document.getElementById("check-btn").innerText = "Continuar";
    }

    // Carregar primeira questão ao abrir
    loadQuestion();
</script>

</body>
</html>
