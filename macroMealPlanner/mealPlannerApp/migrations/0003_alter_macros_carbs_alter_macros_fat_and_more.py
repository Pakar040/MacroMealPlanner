# Generated by Django 5.0.7 on 2024-07-30 06:31

import mealPlannerApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mealPlannerApp', '0002_alter_macros_options_alter_macros_carbs_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='macros',
            name='carbs',
            field=models.DecimalField(decimal_places=0, max_digits=4, validators=[mealPlannerApp.models.validate_non_empty]),
        ),
        migrations.AlterField(
            model_name='macros',
            name='fat',
            field=models.DecimalField(decimal_places=0, max_digits=4, validators=[mealPlannerApp.models.validate_non_empty]),
        ),
        migrations.AlterField(
            model_name='macros',
            name='protein',
            field=models.DecimalField(decimal_places=0, max_digits=4, validators=[mealPlannerApp.models.validate_non_empty]),
        ),
    ]
