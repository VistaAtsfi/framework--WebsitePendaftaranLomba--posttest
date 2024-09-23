from django.db import models
from .models.admin import Admin
from .models.jurusan import Jurusan
from .models.lomba import Lomba
from .models.peserta import Peserta

class PesertaLomba(models.Model):
    nama = models.CharField(max_length=100)
    email = models.EmailField()
    lomba = models.CharField(max_length=100)

    def __str__(self):
        return self.nama
