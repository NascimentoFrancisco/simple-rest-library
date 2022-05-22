from distutils.command.upload import upload
from doctest import master
from django.db import models

# Create your models here.

#função que retorna uma instanicia do livro para ser referencia para a imahem do livro no bd
def upload_image_book(instance, filename):
    return f'{instance.id}-{filename}'

class Books(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    realese_year = models.IntegerField()
    create_at = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to = upload_image_book, blank = True, null = True)
