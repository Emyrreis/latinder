from django.db import models
from django.contrib.auth.models import User
from datetime import date # 1. Adicione esta importação

# ... modelo Owner ...
class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Pet(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    bio = models.TextField()
    birth_date = models.DateField()

    # 2. ADICIONE ESTA PROPRIEDADE
    @property
    def age(self):
        today = date.today()
        # Calcula a idade subtraindo o ano de hoje pelo ano de nascimento,
        # e ajusta caso o aniversário ainda não tenha passado este ano.
        age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return age

    def __str__(self):
        return self.name

# ... modelo PetPhoto ...
class PetPhoto(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='pet_photos/')

    def __str__(self):
        return f"Photo for {self.pet.name}"