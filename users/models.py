from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(default="")
    phone = models.CharField(max_length=11)
    description = models.CharField(max_length=200)
    store_name = models.CharField(max_length=20)
    rating = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])

    def __str__(self):
        return self.name
