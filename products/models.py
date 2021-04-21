from django.db import models
from django.core.validators import *


# Create your models here.

from users.models import User

category_choice =(
    ("KIDDIES_FEMALE", "KIDDIES_FEMALE"),
    ("MEN", "MEN"),
    ("WOMEN", "WOMEN"),
    ("CATEGORY", "CATEGORY"),
    ("KIDDIES_MALE", "KIDDIES_MALE"),
)


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    name = models.CharField(max_length=20)
    product_image = models.ImageField(upload_to="media")
    description = models.CharField(max_length=200)
    category = models.CharField(max_length=100, choices=category_choice, default="CATEGORY")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])

    def __str__(self):
        return self.name
