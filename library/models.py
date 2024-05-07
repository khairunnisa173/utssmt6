from django.db import models
from django.core.validators import MaxLengthValidator


# Create your models here.
class Perpus(models.Model):
    nama = models.CharField(max_length=100)
    alamat = models.TextField(max_length=255)
    no_telp = models.CharField(max_length=12, validators=[MaxLengthValidator(12)])
    

    def __str__(self):
        return self.title
