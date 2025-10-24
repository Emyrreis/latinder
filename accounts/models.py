# Em accounts/models.py
from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # ADICIONEI ESTE CAMPO
    profile_picture = models.ImageField(upload_to='owner_pictures/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def age(self):
        if self.birth_date:
            today = date.today()
            age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
            return age
        return None # Retorna None se não houver data de nascimento

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
    
    #------------------------------------------------------------------------- Sprint 2 a partir daqui --------------------------------------------------#

    # No final de accounts/models.py

# ... (modelos Owner, Pet, PetPhoto existentes) ...

# ADICIONE ESTE NOVO MODELO
class Swipe(models.Model):
    # O pet que está fazendo a ação de deslizar
    swiper = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='swipes_made')
    # O pet que está sendo avaliado
    swiped = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='swipes_received')
    # True se foi um 'like', False se foi um 'pass'
    liked = models.BooleanField()
    # Data e hora em que a ação ocorreu, preenchido automaticamente
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        action = "Liked" if self.liked else "Passed"
        return f"{self.swiper.name} {action} {self.swiped.name}"