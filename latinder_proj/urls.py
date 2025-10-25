# Esse arquivo define as rotas URL para o projeto Latinder.
# Ele inclui as URLs do aplicativo de contas (accounts)
# e configura o acesso a arquivos de mídia durante o desenvolvimento.
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Definindo as rotas principais do projeto
# Adicionamos a rota para o admin e para o app de contas
# A rota raiz ('') aponta para as URLs definidas no app "accounts"
# Configuração para servir arquivos de mídia em modo de desenvolvimento
# Isso é importante para permitir uploads de usuários, como fotos de perfil
# durante o desenvolvimento local.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')), 
]

# Configuração para servir arquivos de mídia em modo de desenvolvimento
# Isso permite que arquivos enviados pelos usuários sejam acessíveis
# apenas quando o DEBUG está ativado (modo de desenvolvimento)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)