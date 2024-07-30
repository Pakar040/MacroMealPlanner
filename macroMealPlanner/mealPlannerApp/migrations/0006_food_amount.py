# Generated by Django 5.0.7 on 2024-07-30 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mealPlannerApp', '0005_food_units'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=5),
            preserve_default=False,
        ),
    ]