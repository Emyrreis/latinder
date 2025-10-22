from django import forms
# 1. Importe também o modelo PetPhoto
from .models import Pet, PetPhoto
from .models import Owner, Pet, PetPhoto

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



class OwnerEditForm(forms.ModelForm):
    class Meta:
        model = Owner
        # Campos que o usuário poderá editar
        fields = ['bio', 'birth_date', 'state', 'city']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }