from django.db import models

# Create your models here.

class Movie(models.Model):
    name=models.CharField(max_length=30)
    image=models.FileField(upload_to="films",verbose_name="Enter film name")
    description=models.TextField(max_length=200,null=True,blank=True)
    trial=models.FileField(upload_to="fragment",null=True,blank=True)
    
    def __str__(self):
        return self.name