from django.db import models

# Create your models here.

class Customer(models.Model):
    full_name =  models.CharField(max_length=30)
    number_phone = models.CharField(max_length=25, blank=True)
    verified_number_phone = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name



class Product(models.Model):
    title = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='photos')


    def __str__(self):
        return self.title