from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Adicionamos uma rota para a raiz do site apontar para as URLs da conta
    path('', include('accounts.urls')), 
]

# ESTA PARTE É ESSENCIAL
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)