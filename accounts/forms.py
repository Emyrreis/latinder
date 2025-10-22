from django import forms
# 1. Importe também o modelo PetPhoto
from .models import Pet, PetPhoto

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'breed', 'bio', 'birth_date']
        widgets = {
            'birth_date': forms.DateInput(
                attrs={'type': 'date'},
            ),
        }

# 2. ADICIONE ESTE NOVO FORMULÁRIO
class PetPhotoForm(forms.ModelForm):
    class Meta:
        model = PetPhoto
        # O único campo que o usuário precisa preencher é o da imagem
        fields = ['image']