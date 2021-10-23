from django.db import models

# Create your models here.

class Hesap(models.Model):
    isim = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    telefon = models.CharField(max_length=255)
    unvan = models.CharField(max_length=255)
    ozet = models.TextField()
    resim = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.isim