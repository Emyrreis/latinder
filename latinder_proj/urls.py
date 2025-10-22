from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Qualquer URL que comece com 'accounts/' será enviada para o arquivo 'urls.py' do nosso app 'accounts'.
    path('accounts/', include('accounts.urls')),
]
