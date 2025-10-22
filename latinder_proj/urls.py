from django.contrib import admin
from django.urls import path, include
# 1. Importe as configurações e a função static
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
]

# 2. Adicione esta linha no final do arquivo
# Isso só funciona em modo de desenvolvimento (DEBUG=True)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)