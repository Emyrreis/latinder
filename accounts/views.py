from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm

# Tarefa 1.3: Criar a view de cadastro de usuário

class SignUpView(CreateView):
        
        # Usa o formulário de criação de usuário padrão do Django.
        form_class = UserCreationForm

        # Em caso de sucesso no cadastro, redireciona o usuário para a página de login.
         # O 'reverse_lazy' só monta a URL quando ela é realmente necessária.    
        success_url = reverse_lazy('login')

        # O nome do arquivo HTML que será usado para renderizar esta página.
        template_name = 'registration/signup.html'