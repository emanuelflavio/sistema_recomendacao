from django.urls import path
from . import views

app_name = 'recomendacao'

urlpatterns = [
    path('', views.home, name='home'),
    path('perguntas/', views.perguntas, name='perguntas'),
    path('recomendacao/<str:tempo_treino>/<str:grupo_muscular>/<str:objetivo_treino>/<str:frequencia_treino>/<str:limitacoes_fisicas>/<str:preferencias_equipamento>/', views.recomendacao, name='recomendacao'),
]
