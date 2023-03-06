from django.db import models

# Create your models here.
class imgmodel(models.Model):
    first_name=models.CharField(max_length=200)
    second_name=models.CharField(max_length=200)
    #path to upload images to media folder
    img=models.ImageField(upload_to="images/",blank=True)

