from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.http import HttpResponseRedirect

# Importações dos nossos Forms e Models
from .forms import PetForm, PetPhotoForm
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

class HomeView(TemplateView):
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

# View que estava faltando
class OwnerDetailView(LoginRequiredMixin, DetailView):
    model = Owner
    template_name = 'owner_detail.html'