from django import forms
from django.contrib.auth.models import User
from .models import Owner, Pet, PetPhoto

# Formulário para criar e editar um Pet
class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'breed', 'bio', 'birth_date']
        widgets = {
            'birth_date': forms.DateInput(
                attrs={'type': 'date'},
            ),
        }

# Formulário para fazer upload de fotos de um Pet
class PetPhotoForm(forms.ModelForm):
    class Meta:
        model = PetPhoto
        fields = ['image']

# Formulário para editar o perfil completo do Dono (Owner)
class OwnerProfileForm(forms.ModelForm):
    # Campos que pertencem ao modelo User, não ao Owner
    first_name = forms.CharField(max_length=30, label="Nome", required=False)
    last_name = forms.CharField(max_length=150, label="Sobrenome", required=False)

    class Meta:
        model = Owner
        # Lista completa de campos que o usuário pode editar
        fields = ['profile_picture', 'first_name', 'last_name', 'bio', 'birth_date', 'state', 'city']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }

    # Método para inicializar o formulário com dados existentes do User
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.user:
            self.fields['first_name'].initial = self.instance.user.first_name
            self.fields['last_name'].initial = self.instance.user.last_name

    # Método customizado para salvar os dados em ambos os modelos
    def save(self, commit=True):
        # Primeiro, salva o modelo Owner (o formulário principal)
        owner = super().save(commit=False)

        # Pega os dados dos campos extras e salva no modelo User associado
        user = owner.user
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        
        if commit:
            user.save()
            owner.save()

        return owner