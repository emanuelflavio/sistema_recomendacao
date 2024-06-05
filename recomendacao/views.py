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
    "Flexão de Braço": "Exercício que fortalece os músculos peitorais, deltoides e tríceps. Como fazer: 1. Comece na posição de prancha com as mãos um pouco mais largas que a largura dos ombros.\n2. Abaixe o corpo até que o peito quase toque o chão, mantendo o corpo em linha reta.\n3. Empurre de volta para a posição inicial, estendendo os braços completamente.",
    "Supino com Barra": "Excelente para desenvolver o peitoral, os deltoides anteriores e os tríceps. Como Fazer: 1. Deite-se em um banco plano com os pés apoiados no chão.\n2. Segure a barra com as mãos um pouco mais largas que a largura dos ombros.\n3. Abaixe a barra em direção ao peito, mantendo os cotovelos próximos ao corpo.\n4. Empurre a barra de volta para cima, estendendo os braços completamente.",
    "Supino Inclinado": "Focado em fortalecer o peitoral superior e os deltoides anteriores.Como fazer: 1. Deite-se em um banco inclinado em um ângulo de aproximadamente 45 graus.\n2. Segure a barra com as mãos um pouco mais largas que a largura dos ombros.\n3. Abaixe a barra em direção ao peito, mantendo os cotovelos próximos ao corpo.\n4. Empurre a barra de volta para cima, estendendo os braços completamente.",
    "Máquina de Peito": "Alternativa segura para fortalecer os músculos peitorais. Como fazer: Sente-se na máquina de peito com as costas bem apoiadas e os pés firmemente no chão.\nSegure as alças da máquina com as mãos.\nEmpurre as alças para longe do peito, estendendo os braços, até que os braços estejam quase retos.\nTraga as alças de volta para o peito lentamente e repita.",
    "Barra Fixa": "Um dos melhores exercícios para as costas, trabalhando latíssimo do dorso e bíceps. Como fazer: 1. Segure uma barra fixa com as mãos na largura dos ombros, com as palmas voltadas para fora.\n2. Pendure-se na barra, estendendo os braços completamente.\n3. Puxe o corpo para cima até que o queixo esteja acima da barra.\n4. Desça o corpo lentamente até os braços estarem estendidos novamente e repita.",
    "Remada Sentada": "Excelente para trabalhar o latíssimo do dorso, trapézio e bíceps. Como fazer: 1. Sente-se em um banco de remada com os pés apoiados no suporte e as pernas ligeiramente flexionadas.\n2. Segure a barra com as mãos na largura dos ombros.\n3. Mantenha as costas retas e puxe a barra em direção ao abdômen, mantendo os cotovelos próximos ao corpo.\n4. Estenda os braços para frente e repita.",
    "Puxada Alta": "Ótimo para desenvolver o latíssimo do dorso e os deltoides. Como fazer: 1. Sente-se na máquina de puxada alta e ajuste as almofadas para que seus joelhos fiquem seguros.\n2. Segure a barra com as mãos um pouco mais largas que a largura dos ombros.\n3. Puxe a barra em direção ao peito, mantendo os cotovelos apontados para baixo.\n4. Lentamente, retorne a barra à posição inicial e repita.",
    "Levantamento Terra": "Trabalha costas, glúteos e posteriores da coxa. Como fazer: 1. Coloque a barra no chão em frente aos seus pés.\n2. Agache-se para pegar a barra com as mãos um pouco mais largas que a largura dos ombros.\n3. Levante a barra mantendo as costas retas e os quadris para trás até ficar completamente em pé.\n4. Baixe a barra de volta ao chão e repita.",
    "Agachamento Livre": "Essencial para desenvolver quadríceps, glúteos e isquiotibiais. Como fazer: 1. Fique em pé com os pés afastados na largura dos ombros.\n2. Mantenha as costas retas e o olhar para frente.\n3. Desça como se estivesse se sentando em uma cadeira, dobrando os joelhos até as coxas ficarem paralelas ao chão.\n4. Empurre através dos calcanhares para voltar à posição inicial e repita.",
    "Leg Press": "Fortalece quadríceps, glúteos e músculos posteriores das coxas. Como fazer: 1. Sente-se na máquina de leg press com as costas bem apoiadas e os pés firmemente no apoio.\n2. Solte o travamento da máquina e abaixe lentamente os joelhos em direção ao peito.\n3. Empurre os pesos de volta à posição inicial, estendendo completamente as pernas.\n4. Repita o movimento controladamente.",
    "Cadeira Extensora": "Excelente para fortalecer o quadríceps. Como fazer: 1. Sente-se na cadeira com as costas bem apoiadas e os pés posicionados contra a almofada.\n2. Levante os pesos estendendo completamente os joelhos.\n3. Desça os pesos de volta à posição inicial controladamente.\n4. Repita o movimento.",
    "Cadeira Flexora": "Trabalha os músculos posteriores da coxa. Como fazer: 1. Sente-se na cadeira com as costas bem apoiadas e as pernas esticadas.\n2. Flexione os joelhos para trazer o calcanhar em direção ao glúteo.\n3. Estenda os joelhos para retornar à posição inicial.\n4. Repita o movimento controladamente.",
    "Desenvolvimento com Halteres": "Focado em desenvolver os deltoides. Como fazer: 1. Fique em pé com um haltere em cada mão, com os braços ao lado do corpo.\n2. Levante os halteres até os ombros, mantendo os cotovelos dobrados.\n3. Pressione os halteres acima da cabeça até que os braços estejam estendidos.\n4. Baixe os halteres de volta à posição inicial e repita.",
    "Elevação Lateral": "Excelente para desenvolver os deltoides laterais. Como fazer: 1. Fique em pé com um haltere em cada mão, com os braços ao lado do corpo.\n2. Levante os halteres para os lados até que os braços estejam paralelos ao chão.\n3. Mantenha os cotovelos levemente flexionados durante todo o movimento.\n4. Baixe os halteres de volta à posição inicial e repita.",
    "Elevação Frontal": "Trabalha principalmente os deltoides anteriores. Como fazer:1. Fique em pé com um haltere em cada mão, com os braços estendidos na frente do corpo.\n2. Levante os halteres à frente até a altura dos ombros, mantendo os braços retos.\n3. Mantenha os cotovelos levemente flexionados durante todo o movimento.\n4. Baixe os halteres de volta à posição inicial e repita.",
    "Remada Alta": "Focado em desenvolver os deltoides posteriores e trapézio. Como fazer: 1. Fique em pé com um haltere em cada mão, com os braços estendidos na frente do corpo.\n2. Levante os halteres para cima e para trás, mantendo os cotovelos levemente flexionados.\n3. Concentre-se em contrair os músculos das costas enquanto levanta os halteres.\n4. Baixe os halteres de volta à posição inicial e repita.",
    "Rosca Direta": "Fortalece os músculos do bíceps braquial. Como fazer: 1. Fique em pé com um haltere em cada mão, com os braços estendidos ao longo do corpo e as palmas voltadas para a frente.\n2. Flexione os cotovelos para levantar os halteres em direção aos ombros.\n3. Mantenha os cotovelos próximos ao corpo durante todo o movimento.\n4. Baixe os halteres de volta à posição inicial e repita.",
    "Tríceps Pulley": "Excelente para trabalhar os tríceps. Como fazer: Fique de frente para a máquina de polia alta com uma barra reta anexada à parte superior.\n2. Agarre a barra com as mãos na largura dos ombros e os cotovelos estendidos.\n3. Mantendo os cotovelos próximos ao corpo, puxe a barra para baixo até que os braços estejam completamente estendidos.\n4. Lentamente, retorne a barra à posição inicial e repita.",
    "Rosca Inversa": "Trabalha os músculos do antebraço e o bíceps. Como fazer: 1. Fique em pé com um haltere em cada mão, com os braços estendidos ao longo do corpo e as palmas voltadas para trás.\n2. Flexione os cotovelos para levantar os halteres em direção aos ombros.\n3. Mantenha os cotovelos próximos ao corpo durante todo o movimento.\n4. Baixe os halteres de volta à posição inicial e repita.",
    "Tríceps Coice": "Ótimo para fortalecer os músculos tríceps. Como fazer: 1. Segure um haltere com uma das mãos e ajoelhe-se em um banco.\n2. Incline o tronco para a frente e apoie o cotovelo no joelho.\n3. Mantenha o braço em um ângulo de 90 graus e estenda o antebraço para trás.\n4. Retorne o antebraço à posição inicial e repita.",
    "Prancha Abdominal": "Fortalece os músculos abdominais e o core. Como fazer: 1. Deite-se de bruços com os cotovelos dobrados e os antebraços apoiados no chão.\n2. Levante o corpo, apoiando-se nos cotovelos e nos dedos dos pés, mantendo o corpo reto.\n3. Mantenha essa posição, contraindo os músculos abdominais, por 20-60 segundos.\n4. Retorne à posição inicial e repita.",
    "Crunch": "Focado em fortalecer os músculos abdominais. Como fazer: 1. Deite-se de costas com os joelhos dobrados e os pés apoiados no chão.\n2. Coloque as mãos atrás da cabeça ou cruzadas sobre o peito.\n3. Levante os ombros em direção aos joelhos, contraindo os músculos abdominais.\n4. Retorne à posição inicial e repita.",
    "Elevação de Pernas": "Trabalha principalmente os músculos abdominais inferiores. Como fazer: 1. Deite-se de costas com as pernas estendidas e as mãos ao lado do corpo.\n2. Levante as pernas em direção ao teto, mantendo-as retas.\n3. Abaixe as pernas lentamente de volta à posição inicial, mantendo o controle.\n4. Repita o movimento.",
    "Supra": "Fortalece os músculos oblíquos e abdominais. Como fazer: 1. Deite-se de lado com o corpo estendido e apoiado no antebraço.\n2. Levante o quadril do chão, mantendo o corpo em linha reta.\n3. Mantenha essa posição por alguns segundos, contraindo os músculos abdominais.\n4. Retorne à posição inicial e repita do outro lado."
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

recomendacao_tempo_treino = {
    "nunca": "É importante começar devagar e progredir gradualmente. Recomendamos começar com treinos curtos e aumentar a duração gradualmente conforme você se sentir mais confortável.",
    "algum tempo": "Você já tem alguma experiência, então pode considerar aumentar a intensidade e a duração dos seus treinos gradualmente para continuar progredindo.",
    "muito tempo": "Você tem bastante experiência! Certifique-se de variar seus treinos para evitar estagnação e lesões. Considere incluir treinos de força, resistência e flexibilidade para manter um bom equilíbrio."
}

recomendacao_objetivo_treino = {
    "perda de peso": "Para perda de peso, é importante focar em exercícios cardiovasculares e em uma dieta balanceada. Recomenda-se também incluir treinos de alta intensidade intercalados com períodos de descanso.",
    "ganho de massa": "Para ganho de massa muscular, é essencial focar em exercícios de musculação que visem o aumento da massa magra. Além disso, uma alimentação rica em proteínas e carboidratos complexos é fundamental.",
    "manter forma": "Para manter a forma, é importante manter uma rotina de exercícios regulares que inclua uma combinação de cardio, musculação e exercícios de flexibilidade. Uma dieta equilibrada também é essencial.",
    "melhorar condicionamento": "Para melhorar o condicionamento físico, é recomendado focar em exercícios aeróbicos, como corrida, natação ou ciclismo, além de treinos de resistência e flexibilidade."
}


def home(request):
    return render(request, 'recomendacao/home.html')


def perguntas(request):
    if request.method == "POST":
        tempo_treino = request.POST.get("tempo_treino")
        grupo_muscular = request.POST.get("grupo_muscular")
        objetivo = request.POST.get('objetivo')
        return redirect('recomendacao:recomendacao', tempo_treino=tempo_treino, grupo_muscular=grupo_muscular, objetivo=objetivo)
    return render(request, 'recomendacao/perguntas.html')


def recomendacao(request, tempo_treino, grupo_muscular, objetivo):
    grupo_muscular = grupo_muscular.lower()
    if grupo_muscular not in exercicios_por_grupo_muscular:
        return render(request, 'recomendacao/error.html', {"message": "Grupo muscular não reconhecido."})

    exercicios = exercicios_por_grupo_muscular[grupo_muscular]
    random.shuffle(exercicios)
    recomendados = exercicios[:3]
    rec_tempo = recomendacao_tempo_treino[tempo_treino]
    rec_objetivo = recomendacao_objetivo_treino[objetivo]
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
        "tempo_treino": tempo_treino.capitalize(),
        "grupo_muscular": grupo_muscular.capitalize(),
        "tempo_rec": rec_tempo,
        "obj_rec": rec_objetivo,
        "objetivo": objetivo.capitalize(),

    }

    return render(request, 'recomendacao/recomendacao.html', context)
