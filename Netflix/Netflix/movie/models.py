from django.db import models

# Create your models here.

class Category(models.Model):
    isim=models.CharField(max_length=50)
    def __str__(self):
        return self.isim
    
class Movie(models.Model):
    name=models.CharField(max_length=50)
    image=models.FileField(upload_to='films', verbose_name="upload image",null=True,blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return self.name