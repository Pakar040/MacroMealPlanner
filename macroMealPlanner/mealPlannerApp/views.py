from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import SignupForm, LoginForm

# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect(reverse('mealPlannerApp:login'))
    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('mealPlannerApp:macros'))
            else:
                messages.error(request, "Invalid Username or Password")
        else:
            messages.error(request, "Invalid Username or Password")
    else:
        form = LoginForm()

    return render(request, 'mealPlannerApp/login.html', {'form': form})

def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('mealPlannerApp:macros'))
        else:
            messages.error(request, form.errors.as_text())

    else:
        form = SignupForm()

    return render(request, 'mealPlannerApp/signup.html', {'form': form})

def macros_view(request):
    return render(request, 'mealPlannerApp/macros.html')

def food_view(request):
    return render(request, 'mealPlannerApp/food.html')

def plan_view(request):
    return render(request, 'mealPlannerApp/plan.html')