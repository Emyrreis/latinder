from django.urls import path
# Vamos importar as views de autenticação diretamente
from django.contrib.auth import views as auth_views
from .views import SignUpView

from .views import SignUpView, HomeView

urlpatterns = [
    # Aqui definimos a rota e damos o apelido (name) 'login' explicitamente
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),

    # Fazemos o mesmo para o logout
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # E a nossa view de cadastro continua aqui
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', HomeView.as_view(), name='home'),
]