from mealPlannerApp.testing.script import generate_macros, generate_users, generate_foods
from django.contrib.auth.models import User
from mealPlannerApp.models import Macros, Food

choice = input("Enter 'c' to Create Data or enter 'd' to Delete Data: ").lower()

if choice == 'd':
   Macros.objects.all().delete()
   Food.objects.all().delete()
   User.objects.filter(is_staff=False).delete()
   print("Successfully deleted all Users, Macros, and Foods!")
elif choice == 'c':
   num_users = int(input("Enter the number of users you want to create: "))
   num_macros = int(input("Enter the number of macros you want to create: "))
   num_foods = int(input("Enter the number of foods you want to create: "))
   generate_users(num_users=num_users)
   generate_macros(num_macros=num_macros)
   generate_foods(num_foods=num_foods)
   print(f"Successfully add {num_users} User(s) and {num_macros} Macro(s) and {num_foods} Food(s)!")
else:
   print("Not an option.")
