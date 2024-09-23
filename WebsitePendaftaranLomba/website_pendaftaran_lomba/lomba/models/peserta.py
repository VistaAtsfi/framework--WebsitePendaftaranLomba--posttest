from django.db import models
from .lomba import Lomba

class Peserta(models.Model):
    nama = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    no_hp = models.CharField(max_length=13, unique=True)
    alamat = models.CharField(max_length=255)
    lomba = models.ForeignKey(Lomba, on_delete=models.CASCADE, related_name='peserta')

    def __str__(self):
        return self.nama
