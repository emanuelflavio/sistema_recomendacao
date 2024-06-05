from django.shortcuts import render, redirect
import random

# Definindo os exercícios por grupo muscular
exercicios_por_grupo_muscular = {
    "peito": ["Flexão de Braço", "Supino com Barra", "Supino Inclinado", "Máquina de Peito"],
    "costas": ["Barra Fixa", "Remada Sentada", "Puxada Alta", "Levantamento Terra"],
    "pernas": ["Agachamento Livre", "Leg Press", "Cadeira Extensora", "Cadeira Flexora"],
    "ombros": ["Desenvolvimento com Halteres", "Elevação Lateral", "Elevação Frontal", "Remada Alta"],
    "braços": ["Rosca Direta", "Tríceps Pulley", "Rosca Inversa", "Tríceps Coice"],
    "abdômen": ["Prancha Abdominal", "Crunch", "Elevação de Pernas", "Supra"]
}

# Explicação dos exercícios
explicacao_exercicios = {
    "Flexão de Braço": "Exercício que fortalece os músculos peitorais, deltoides e tríceps.",
    "Supino com Barra": "Excelente para desenvolver o peitoral, os deltoides anteriores e os tríceps.",
    "Supino Inclinado": "Focado em fortalecer o peitoral superior e os deltoides anteriores.",
    "Máquina de Peito": "Alternativa segura para fortalecer os músculos peitorais.",
    "Barra Fixa": "Um dos melhores exercícios para as costas, trabalhando latíssimo do dorso e bíceps.",
    "Remada Sentada": "Excelente para trabalhar o latíssimo do dorso, trapézio e bíceps.",
    "Puxada Alta": "Ótimo para desenvolver o latíssimo do dorso e os deltoides.",
    "Levantamento Terra": "Trabalha costas, glúteos e posteriores da coxa.",
    "Agachamento Livre": "Essencial para desenvolver quadríceps, glúteos e isquiotibiais.",
    "Leg Press": "Fortalece quadríceps, glúteos e músculos posteriores das coxas.",
    "Cadeira Extensora": "Excelente para fortalecer o quadríceps.",
    "Cadeira Flexora": "Trabalha os músculos posteriores da coxa.",
    "Desenvolvimento com Halteres": "Focado em desenvolver os deltoides.",
    "Elevação Lateral": "Excelente para desenvolver os deltoides laterais.",
    "Elevação Frontal": "Trabalha principalmente os deltoides anteriores.",
    "Remada Alta": "Focado em desenvolver os deltoides posteriores e trapézio.",
    "Rosca Direta": "Fortalece os músculos do bíceps braquial.",
    "Tríceps Pulley": "Excelente para trabalhar os tríceps.",
    "Rosca Inversa": "Trabalha os músculos do antebraço e o bíceps.",
    "Tríceps Coice": "Ótimo para fortalecer os músculos tríceps.",
    "Prancha Abdominal": "Fortalece os músculos abdominais e o core.",
    "Crunch": "Focado em fortalecer os músculos abdominais.",
    "Elevação de Pernas": "Trabalha principalmente os músculos abdominais inferiores.",
    "Supra": "Fortalece os músculos oblíquos e abdominais."
}

# Links dos exercícios
exercicios_links = {
    "Flexão de Braço": "https://www.youtube.com/watch?v=IODxDxX7oi4",
    "Supino com Barra": "https://www.youtube.com/watch?v=rT7DgCr-3pg",
    "Supino Inclinado": "https://www.youtube.com/watch?v=DbFgADa2PL8",
    "Máquina de Peito": "https://www.youtube.com/watch?v=MQHiZk8i2nU",
    "Barra Fixa": "https://www.youtube.com/watch?v=eGo4IYlbE5g",
    "Remada Sentada": "https://www.youtube.com/watch?v=GZbfZ033f74",
    "Puxada Alta": "https://www.youtube.com/watch?v=CAwf7n6Luuc",
    "Levantamento Terra": "https://www.youtube.com/watch?v=op9kVnSso6Q",
    "Agachamento Livre": "https://www.youtube.com/watch?v=Dy28eq2PjcM",
    "Leg Press": "https://www.youtube.com/watch?v=LfhGmaP9dLs",
    "Cadeira Extensora": "https://www.youtube.com/watch?v=YyvSfVjQeL0",
    "Cadeira Flexora": "https://www.youtube.com/watch?v=ljOxo0s33sI",
    "Desenvolvimento com Halteres": "https://www.youtube.com/watch?v=B-aVuyhvLHU",
    "Elevação Lateral": "https://www.youtube.com/watch?v=3VcKaXpzqRo",
    "Elevação Frontal": "https://www.youtube.com/watch?v=GSzP1K2rVlU",
    "Remada Alta": "https://www.youtube.com/watch?v=KB3uGf3DL8Y",
    "Rosca Direta": "https://www.youtube.com/watch?v=zC3nLlEvin4",
    "Tríceps Pulley": "https://www.youtube.com/watch?v=2-LAMcpzODU",
    "Rosca Inversa": "https://www.youtube.com/watch?v=MEyLWigabCI",
    "Tríceps Coice": "https://www.youtube.com/watch?v=2-LAMcpzODU",
    "Prancha Abdominal": "https://www.youtube.com/watch?v=pSHjTRCQxIw",
    "Crunch": "https://www.youtube.com/watch?v=Xyd_fa5zoEU",
    "Elevação de Pernas": "https://www.youtube.com/watch?v=JB2oyawG9KI",
    "Supra": "https://www.youtube.com/watch?v=5cWtCmqaxMw"
}

# Exercícios a evitar com base nas limitações físicas
limitacoes_exercicios = {
    "lesao_no_joelho": ["Agachamento Livre", "Leg Press"],
    "lesao_no_ombro": ["Desenvolvimento com Halteres", "Elevação Lateral", "Elevação Frontal"],
    "problemas_nas_costas": ["Levantamento Terra", "Agachamento Livre"]
}

def home(request):
    return render(request, 'recomendacao/home.html')

def perguntas(request):
    if request.method == "POST":
        tempo_treino = request.POST.get("tempo_treino")
        grupo_muscular = request.POST.get("grupo_muscular")
        objetivo_treino = request.POST.get("objetivo_treino")
        frequencia_treino = request.POST.get("frequencia_treino")
        limitacoes_fisicas = request.POST.get("limitacoes_fisicas")
        preferencias_equipamento = request.POST.get("preferencias_equipamento")
        
        return redirect('recomendacao:recomendacao', tempo_treino=tempo_treino, grupo_muscular=grupo_muscular, objetivo_treino=objetivo_treino, frequencia_treino=frequencia_treino, limitacoes_fisicas=limitacoes_fisicas, preferencias_equipamento=preferencias_equipamento)
    return render(request, 'recomendacao/perguntas.html')

def recomendacao(request, tempo_treino, grupo_muscular, objetivo_treino, frequencia_treino, limitacoes_fisicas, preferencias_equipamento):
    grupo_muscular = grupo_muscular.lower()
    if grupo_muscular not in exercicios_por_grupo_muscular:
        return render(request, 'recomendacao/error.html', {"message": "Grupo muscular não reconhecido."})

    exercicios = exercicios_por_grupo_muscular[grupo_muscular]

    # Adicionando sugestões gerais baseadas no tempo de treino e objetivo do usuário
    sugestoes = []
    if tempo_treino == "nunca":
        sugestoes.append("Recomenda-se começar com alongamentos e um aquecimento cardiovascular leve antes do treino.")
    elif tempo_treino == "muito_tempo":
        sugestoes.append("Considere aumentar a carga dos exercícios para continuar a progressão.")

    if objetivo_treino == "perda_de_peso":
        sugestoes.append("Inclua exercícios cardiovasculares intensos e de alta repetição para ajudar na perda de peso.")
    elif objetivo_treino == "ganho_de_massa":
        sugestoes.append("Concentre-se em exercícios com carga pesada e baixa repetição para aumentar a massa muscular.")
    elif objetivo_treino == "manter_forma":
        sugestoes.append("Mantenha um equilíbrio entre exercícios de força e cardiovasculares para manter a forma.")
    elif objetivo_treino == "melhorar_condicionamento":
        sugestoes.append("Inclua exercícios variados e de alta intensidade para melhorar o condicionamento físico geral.")

    if frequencia_treino in ["1-2", "3-4"]:
        sugestoes.append("Recomenda-se treinar mais de um grupo muscular por sessão, devido à frequência de treino limitada.")

    # Filtrando exercícios com base em limitações físicas
    exercicios_filtrados = [ex for ex in exercicios if ex not in limitacoes_exercicios.get(limitacoes_fisicas, [])]

    # Filtrando exercícios com base em preferências de equipamento
    if preferencias_equipamento != "todos":
        exercicios_filtrados = [ex for ex in exercicios_filtrados if preferencias_equipamento in explicacao_exercicios[ex].lower()]

    # Garantindo que sempre haja exercícios disponíveis
    if not exercicios_filtrados:
        exercicios_filtrados = exercicios  # Se nenhum exercício passar pela filtragem, usar todos os exercícios do grupo muscular

    random.shuffle(exercicios_filtrados)
    recomendados = exercicios_filtrados[:3]
    explicacoes_links = [
        {
            "exercicio": exercicio,
            "explicacao": explicacao_exercicios.get(exercicio, "Sem explicação disponível."),
            "link": exercicios_links.get(exercicio, "#")
        }
        for exercicio in recomendados
    ]

    context = {
        "explicacoes_links": explicacoes_links,
        "tempo_treino": tempo_treino,
        "grupo_muscular": grupo_muscular.capitalize(),
        "objetivo_treino": objetivo_treino,
        "frequencia_treino": frequencia_treino,
        "limitacoes_fisicas": limitacoes_fisicas,
        "preferencias_equipamento": preferencias_equipamento,
        "sugestoes": sugestoes
    }

    return render(request, 'recomendacao/recomendacao.html', context)
