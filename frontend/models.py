from django.db import models


class Berita(models.Model):
    judul = models.CharField(max_length=256)
    isi = models.TextField(null=True, blank=True)
    tanggal = models.DateTimeField(auto_now=True)
    gambar = models.ImageField(null=True, blank=True)
    
    def __str__(self) -> str:
        return self.judul