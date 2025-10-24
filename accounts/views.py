from django.urls import reverse_lazy
# A correção está nesta linha, removemos o ", Or"
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.base import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.http import HttpResponseRedirect
import json
from django.http import JsonResponse
from django.views import View
#-------------------------------- Sprint 2 ----------------------------------#
# 1. Adicione a importação para ListView
from django.views.generic import ListView
from .models import Pet, Owner, PetPhoto, Swipe # 2. Adicione Swipe
#-------------------------------------------------------------------------#

# Importações dos nossos Forms e Models
from .forms import PetForm, PetPhotoForm, OwnerProfileForm
from .models import Pet, Owner, PetPhoto

# --- Nossas Views ---

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        Owner.objects.create(user=self.object)
        return response

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

class PetCreateView(LoginRequiredMixin, CreateView):
    model = Pet
    form_class = PetForm
    template_name = 'pet_form.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user.owner
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('pet_detail', kwargs={'pk': self.object.pk})

class PetDetailView(DetailView):
    model = Pet
    template_name = 'pet_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photo_form'] = PetPhotoForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = PetPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.pet = self.object
            photo.save()
            return HttpResponseRedirect(self.request.path_info)
        else:
            context = self.get_context_data()
            context['photo_form'] = form
            return self.render_to_response(context)

class OwnerDetailView(LoginRequiredMixin, DetailView):
    model = Owner
    template_name = 'owner_detail.html'

class OwnerUpdateView(LoginRequiredMixin, UpdateView):
    model = Owner
    form_class = OwnerProfileForm
    template_name = 'owner_form.html'
    
    def get_success_url(self):
        return reverse_lazy('owner_detail', kwargs={'pk': self.object.pk})

    def get_object(self, queryset=None):
        return self.request.user.owner
    

# No final de accounts/views.py

class PetUpdateView(LoginRequiredMixin, UpdateView):
    model = Pet
    form_class = PetForm # Podemos reutilizar o mesmo PetForm que criamos!
    template_name = 'pet_form.html' # E também o mesmo template!

    def get_success_url(self):
        # Após editar, volta para a página de detalhes do pet
        return reverse_lazy('pet_detail', kwargs={'pk': self.object.pk})

    def get_queryset(self):
        # Esta é a checagem de segurança!
        # A view só poderá encontrar e editar pets que pertencem ao usuário logado.
        return Pet.objects.filter(owner=self.request.user.owner)
    


# 3. ADICIONE ESTA NOVA VIEW NO FINAL DO ARQUIVO
class SwipeView(LoginRequiredMixin, ListView):
    model = Pet
    template_name = 'swipe.html'
    context_object_name = 'pets_to_swipe' # Nome da lista no template

    def get_queryset(self):
        # Pega o pet do usuário logado. Se não tiver, retorna uma lista vazia.
        try:
            user_pet = self.request.user.owner.pet_set.first()
        except (Owner.DoesNotExist, AttributeError):
            return Pet.objects.none()

        # Se o usuário não tem pet, não pode ver outros.
        if not user_pet:
            return Pet.objects.none()

        # Pega a lista de IDs de pets que o usuário já avaliou (swiped)
        swiped_pet_ids = Swipe.objects.filter(swiper=user_pet).values_list('swiped_id', flat=True)

        # Busca todos os pets, excluindo:
        # 1. O próprio pet do usuário.
        # 2. Os pets que já foram avaliados.
        queryset = Pet.objects.exclude(id=user_pet.id).exclude(id__in=swiped_pet_ids)
        
        return queryset
    


# 2. ADICIONE ESTA NOVA VIEW DE API NO FINAL DO ARQUIVO
class ProcessSwipeView(LoginRequiredMixin, View):
    
    def post(self, request, *args, **kwargs):
        try:
            # Pega o pet do usuário logado
            swiper_pet = request.user.owner.pet_set.first()
            if not swiper_pet:
                return JsonResponse({'status': 'error', 'message': 'User has no pet.'}, status=400)

            # Carrega os dados enviados pelo JavaScript
            data = json.loads(request.body)
            swiped_pet_id = data.get('swiped_pet_id')
            liked = data.get('liked')

            # Encontra o pet que foi avaliado
            swiped_pet = Pet.objects.get(id=swiped_pet_id)

            # Cria e salva o objeto Swipe no banco de dados
            Swipe.objects.create(
                swiper=swiper_pet,
                swiped=swiped_pet,
                liked=liked
            )
            
            # Responde ao JavaScript com uma mensagem de sucesso
            return JsonResponse({'status': 'success'})

        except Exception as e:
            # Em caso de qualquer erro, responde com uma mensagem de erro
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)