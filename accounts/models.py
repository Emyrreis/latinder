from django.db import models
from django.contrib.auth.models import User

# Tarefa 1.1: Criar os modelos Owner, Pet e PetPhoto
#aqui fica as definições dos modelos (tabelas do banco de dados)
class Owner(models.Model):
        # Estende o modelo User padrão do Django. O CASCADE significa que se o User for deletado,
        # o perfil do Owner associado a ele também será.
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        bio = models.TextField(blank=True, null=True) # Campo opcional para uma biografia do dono do pet
        created_at = models.DateTimeField(auto_now_add=True) # Data de criação do perfil do dono do pet

        def __str__(self):
            return self.user.username

class Pet(models.Model):
        # Chave Estrangeira para Owner: Liga o pet ao seu dono.
        # Se um dono for deletado, todos os seus pets também serão (CASCADE).
        owner = models.ForeignKey(Owner, on_delete=models.CASCADE) 
        name = models.CharField(max_length=50)
        age = models.IntegerField()
        breed = models.CharField(max_length=40)
        bio = models.TextField()
        birth_date = models.DateField()

        def __str__(self):
            return self.name


class PetPhoto(models.Model):
        # Chave Estrangeira para Pet: Liga a foto ao pet correspondente.
        # Se um pet for deletado, todas as suas fotos também serão (CASCADE).
        pet = models.ForeignKey(Pet, on_delete=models.CASCADE) 
        # O upload_to='pet_photos/' diz ao Django para salvar as imagens
        # em uma pasta chamada 'pet_photos' dentro da sua pasta de mídias.
        photo = models.ImageField(upload_to='pet_photos/') # Campo para armazenar a foto do pet


        def __str__(self):
            return f"Photo of {self.pet.name} "