from django.db import models

class Lomba(models.Model):
    nama = models.CharField(max_length=255)
    jenis_lomba = models.CharField(max_length=100)
    tanggal = models.DateField()
    lokasi = models.CharField(max_length=255)

    def __str__(self):
        return self.nama
