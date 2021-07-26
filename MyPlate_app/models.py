from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class FoodItems(models.Model):
    name = models.CharField(max_length=100, unique=True)
    calories = models.DecimalField(decimal_places=2, max_digits=10)
    image = models.ImageField(upload_to='images', null=True)

    def str(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'FoodItems'

class SetGoal(models.Model):
    goal = models.DecimalField(decimal_places=2, max_digits=10)

    def str(self):
        return self.goal

class Previous_records(models.Model):
    user = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    totalCalories = models.DecimalField(decimal_places=2, max_digits=10)
    goal_set = models.DecimalField(decimal_places=2, max_digits=10)

    def str(self):
        return self.user