from django import forms
from .models import Pet

class PetForm(forms.ModelForm):
    class Meta:

        #Diz ao django que este formulário é para o modelo Pet
        model = Pet
        #Lista os campos do modelo que devem aparecer no formulário
        fields = ['name', 'breed', 'bio', 'birth_date']

        #customizando widgets para melhorar a aparência do formulário
        widgets = {

            'birth_date': forms.DateInput(attrs= {'type': 'date',}),

        }