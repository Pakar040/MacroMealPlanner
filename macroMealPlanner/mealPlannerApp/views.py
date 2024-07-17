from django.shortcuts import render

# Create your views here.
def login_view(request):
    return render(request, 'mealPlannerApp/login.html')

def signup_view(request):
    return render(request, 'mealPlannerApp/signup.html')

def macros_view(request):
    return render(request, 'mealPlannerApp/macros.html')

def food_view(request):
    return render(request, 'mealPlannerApp/food.html')

def plan_view(request):
    return render(request, 'mealPlannerApp/plan.html')