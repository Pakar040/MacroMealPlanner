from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

def validate_non_empty(value):
    if value == '':
        raise ValidationError('This field cannot be empty.')

# Create your models here.
class Macros(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='macros')
    name = models.CharField(max_length=100, validators=[validate_non_empty])
    protein = models.DecimalField(max_digits=4, decimal_places=0, validators=[validate_non_empty])
    fat = models.DecimalField(max_digits=4, decimal_places=0, validators=[validate_non_empty])
    carbs = models.DecimalField(max_digits=4, decimal_places=0, validators=[validate_non_empty])

    class Meta:
        unique_together = ('user', 'name')
        verbose_name_plural = "Macros"

    def __str__(self) -> str:
        return f"{self.user.username} - {self.name}: Fat: {self.fat}cal, Protein: {self.protein}cal, Carbs: {self.carbs}cal"
    
class Food(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='food')
    name = models.CharField(max_length=100)
    units = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    protein = models.DecimalField(max_digits=4, decimal_places=0)
    fat = models.DecimalField(max_digits=4, decimal_places=0)
    carbs = models.DecimalField(max_digits=4, decimal_places=0)

    def __str__(self):
        return f"{self.name} - Protein: {self.protein}cal, Fat: {self.fat}cal, Carbs: {self.carbs}cal"
