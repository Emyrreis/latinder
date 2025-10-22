from django.urls import path
from .views import SignUpView

# Tarefa 1.5: Configurar a rota para a view de cadastro
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]