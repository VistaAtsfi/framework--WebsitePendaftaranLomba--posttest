from django.db import models

class AdminLomba(models.Model):
    nama = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    nomor_ponsel = models.CharField(max_length=15) 
    alamat = models.TextField() 

    def __str__(self):
        return self.nama
