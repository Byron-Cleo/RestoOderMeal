#imports from the django environment
# import random
# import os
# from django.conf import settings

#imports from the django MODEL environment
from django.db import models

#my custom imports
#from restoOrderMealProject.utils import unique_slug_generator,

#

# Create your models here.

class FoodVariety(models.Model):
    food_titile = models.CharField(max_length=120)
    food_slug = models.SlugField(blank=True, unique=True)
    food_description = models.TextField()
    food_price = models.DecimalField(decimal_places=2, max_digits=20, default=50.00)
    timestamp       = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.food_title
