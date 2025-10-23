from django.urls import path
from django.contrib.auth import views as auth_views
# 1. Adicione PetDetailView à importação
from .views import (
    SignUpView, HomeView, PetCreateView, PetDetailView, OwnerDetailView,
    OwnerUpdateView, PetUpdateView
)

urlpatterns = [
    # Rotas de Autenticação
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    

    # Rotas do App
    path('', HomeView.as_view(), name='home'),
    path('pet/add/', PetCreateView.as_view(), name='pet_add'),

    # 2. Adicione esta nova rota dinâmica
    # O <int:pk> é um conversor que captura um número inteiro da URL
    # e o passa para a view como uma variável chamada 'pk' (Primary Key).
    path('pet/<int:pk>/', PetDetailView.as_view(), name='pet_detail'),

    # --- NOVA ROTA ADICIONADA --- Ver detalhes do Owner
    path('profile/<int:pk>/', OwnerDetailView.as_view(), name='owner_detail'),

    path('profile/edit/', OwnerUpdateView.as_view(), name='owner_edit'),

    path('pet/<int:pk>/edit/', PetUpdateView.as_view(), name='pet_edit'),
]