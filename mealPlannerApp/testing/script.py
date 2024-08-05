import os
import django
import random
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'macroMealPlanner.settings')
django.setup()

from django.contrib.auth.models import User
from mealPlannerApp.models import Macros, Food

fake = Faker()

def generate_users(num_users):
   if num_users <= 10:
         num = 1
   elif num_users <= 100:
         num = 10
   else:
         num = 50

   for i in range(num_users):
      username = fake.user_name()
      if not User.objects.filter(username=username).exists():
         user = User.objects.create_user(username=username, password='password')
         user.save()

      if i % num == 0:
         print(f"Creating user {i}/{num_users}")

def generate_macros(num_macros):
   if num_macros <= 10:
      num = 1
   elif num_macros <= 100:
      num = 10
   else:
      num = 50

   users = User.objects.all()
   if not users.exists():
      print("No users available. Generating macros aborted.")
      return
    
   for i in range(num_macros):
      user = random.choice(users)
      name = f"diet{i}"
      if Macros.objects.filter(user=user, name=name).exists():
         continue  # Skip this iteration to avoid violating unique_together constraint
      protein = random.randint(20, 200)
      fat = random.randint(20, 200)
      carbs = random.randint(20, 200)
      macro = Macros(user=user, name=name, protein=protein, fat=fat, carbs=carbs)
      macro.save()
      
      if i % num == 0:
         print(f"Creating macro {i}/{num_macros} for user {user}")

def generate_foods(num_foods):
   if num_foods <= 10:
      num = 1
   elif num_foods <= 100:
      num = 10
   else:
      num = 50
   
   users = User.objects.all()
   if not users.exists():
      print("No users available. Generating macros aborted.")
      return

   for i in range(num_foods):
      user = random.choice(users)
      name = "Steak"
      # if Food.objects.filter(user=user).exists():
      #    continue
      units = "grams"
      amount = round(random.random(), 2)
      protein = random.randint(50, 1000)
      fat = random.randint(50, 1000)
      carbs = random.randint(50, 1000)
      food = Food(user=user, name=name, units=units, amount=amount, protein=protein, fat=fat, carbs=carbs)
      food.save()

      if i % num == 0:
         print(f"Creating food {i}/{num_foods} for user {user}")

      
