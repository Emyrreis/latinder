from django import forms
# 1. Importe também o modelo PetPhoto
from .models import Pet, PetPhoto
from .models import Owner, Pet, PetPhoto
from django.contrib.auth.models import User

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'breed', 'bio', 'birth_date']
        widgets = {
            'birth_date': forms.DateInput(
                attrs={'type': 'date'},
            ),
        }


class PetPhotoForm(forms.ModelForm):
    class Meta:
        model = PetPhoto
        # O único campo que o usuário precisa preencher é o da imagem
        fields = ['image']



class OwnerProfileForm(forms.ModelForm):
    # Campos extras que não estão no modelo Owner
    first_name = forms.CharField(max_length=30, label="Nome")
    last_name = forms.CharField(max_length=150, label="Sobrenome")

    class Meta:
        model = Owner
        fields = ['profile_picture', 'first_name', 'last_name', 'bio', 'birth_date', 'state', 'city']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }

    # Método especial para salvar os dados nos dois modelos
    def save(self, commit=True):
        user = self.instance.user
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()

        return super().save(commit=commit)