from django.db import models

class blogs(models.Model):
    name=models.CharField(max_length=50)
    img=models.ImageField(upload_to='picture')
    catgry = models.CharField(max_length=50)
    dec=models.TextField()
    author=models.CharField(max_length=50)




class second(models.Model):
    name = models.CharField(max_length=50)
    imgs = models.ImageField(upload_to='picture')
    date = models.DateField()

# Create your models here.
