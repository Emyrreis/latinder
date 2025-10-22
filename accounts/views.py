from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Importe o nosso PetForm e os modelos Pet e Owner
from .forms import PetForm
from .models import Pet, Owner


# --- Nossas Views ---

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        # Primeiro, salva o usuário
        response = super().form_valid(form)
        # Depois, cria um objeto Owner ligado a esse usuário
        Owner.objects.create(user=self.object)
        return response

class HomeView(TemplateView):
    template_name = 'home.html'

class PetCreateView(LoginRequiredMixin, CreateView):
    model = Pet
    form_class = PetForm
    template_name = 'pet_form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Pega o objeto do formulário, mas não salva no banco ainda
        form.instance.owner = self.request.user.owner
        # Agora sim, salva o objeto no banco de dados com o dono associado
        return super().form_valid(form)