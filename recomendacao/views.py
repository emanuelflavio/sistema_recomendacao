# recomendacao/views.py
from django.shortcuts import render, redirect
import random

exercicios_por_grupo_muscular = {
    "peito": ["Flexão de Braço", "Supino com Barra", "Supino Inclinado", "Máquina de Peito"],
    "costas": ["Barra Fixa", "Remada Sentada", "Puxada Alta", "Levantamento Terra"],
    "pernas": ["Agachamento Livre", "Leg Press", "Cadeira Extensora", "Cadeira Flexora"],
    "ombros": ["Desenvolvimento com Halteres", "Elevação Lateral", "Elevação Frontal", "Remada Alta"],
    "braços": ["Rosca Direta", "Tríceps Pulley", "Rosca Inversa", "Tríceps Coice"],
    "abdômen": ["Prancha Abdominal", "Crunch", "Elevação de Pernas", "Supra"]
}

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

exercicios_links = {
    "Flexão de Braço": "https://www.youtube.com/watch?v=ZRXFKqUSGaM",
    "Supino com Barra": "https://www.youtube.com/watch?v=9Jo8XwFNot4",
    "Supino Inclinado": "https://www.youtube.com/watch?v=9Jo8XwFNot4",
    "Máquina de Peito": "https://www.youtube.com/watch?v=9Jo8XwFNot4",
    "Barra Fixa": "https://www.youtube.com/watch?v=9Jo8XwFNot4",
    "Remada Sentada": "https://www.youtube.com/watch?v=9Jo8XwFNot4",
    "Puxada Alta": "https://www.youtube.com/watch?v=9Jo8XwFNot4",
    "Levantamento Terra": "https://www.youtube.com/watch?v=9Jo8XwFNot4",
    "Agachamento Livre": "https://www.youtube.com/watch?v=9Jo8XwFNot4",
    "Leg Press": "https://www.youtube.com/watch?v=9Jo8XwFNot4",
    "Cadeira Extensora": "https://www.youtube.com/watch?v=9Jo8XwFNot4",
    "Cadeira Flexora": "https://www.youtube.com/watch?v=9Jo8XwFNot4",
    "Desenvolvimento com Halteres": "https://www.youtube.com/watch?v=9Jo8XwFNot4",
    "Elevação Lateral": "https://www.youtube.com/watch?v=9Jo8XwFNot4",
    "Elevação Frontal": "https://www.youtube.com/watch?v=9Jo8XwFNot4",
    "Remada Alta": "https://www.youtube.com/watch?v=9Jo8XwFNot4",
    "Rosca Direta": "https://www.youtube.com/watch?v=9Jo8XwFNot4",
    "Tríceps Pulley": "https://www.youtube.com/watch?v=9Jo8XwFNot4",
    "Rosca Inversa": "https://www.youtube.com/watch?v=9Jo8XwFNot4",
    "Tríceps Coice": "https://www.youtube.com/watch?v=9Jo8XwFNot4",
    "Prancha Abdominal": "https://www.youtube.com/watch?v=9Jo8XwFNot4",
    "Crunch": "https://www.youtube.com/watch?v=9Jo8XwFNot4",
    "Elevação de Pernas": "https://www.youtube.com/watch?v=9Jo8XwFNot4",
    "Supra": "https://www.youtube.com/watch?v=9Jo8XwFNot4"
}


def home(request):
    return render(request, 'recomendacao/home.html')


def perguntas(request):
    if request.method == "POST":
        tempo_treino = request.POST.get("tempo_treino")
        grupo_muscular = request.POST.get("grupo_muscular")
        return redirect('recomendacao:recomendacao', tempo_treino=tempo_treino, grupo_muscular=grupo_muscular)
    return render(request, 'recomendacao/perguntas.html')


def recomendacao(request, tempo_treino, grupo_muscular):
    grupo_muscular = grupo_muscular.lower()
    if grupo_muscular not in exercicios_por_grupo_muscular:
        return render(request, 'recomendacao/error.html', {"message": "Grupo muscular não reconhecido."})

    exercicios = exercicios_por_grupo_muscular[grupo_muscular]
    random.shuffle(exercicios)
    recomendados = exercicios[:3]
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
        "grupo_muscular": grupo_muscular.capitalize()
    }

    return render(request, 'recomendacao/recomendacao.html', context)
