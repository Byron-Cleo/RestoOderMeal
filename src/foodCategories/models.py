from django.db import models

from foodCategories.models import FoodCategory

# Create your models here.

class FoodCategory(models.Model):
    FOOD_CATEGORY_TYPE = (
        ('breakfast', 'BreakFast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
    )

    FOOD_SPECIAL_DAY = (
        ('monday_special', 'Monday Special'),
        ('cranchy_tuesday', 'Cranchy Tuesday'),
        ('weno_tamutamu', 'Weno TamuTamu'),        
    )

    cat_title = models.CharField(max_length=120, choices=FOOD_CATEGORY_TYPE, default="Please Select First")
    cat_specialday = models.CharField(max_length=120, choices=FOOD_SPECIAL_DAY, default="Please Select First")
    food_category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)


    def __str__(self):
        return self.cat_title
