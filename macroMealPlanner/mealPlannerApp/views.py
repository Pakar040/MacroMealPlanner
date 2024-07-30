from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignupForm, LoginForm, MacrosForm
from .models import Macros

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

@login_required
def macros_view(request):
    if request.method == "POST":
        form = MacrosForm(request.POST)

        if form.is_valid():
            macros = form.save(commit=False)
            macros.user = request.user
            macros.save()
            return redirect(reverse('mealPlannerApp:macros'))

    else:
        form = MacrosForm()

    return render(request, 'mealPlannerApp/macros.html', {
        'form': form,
        'macros_list': Macros.objects.filter(user=request.user)
        })

@login_required
def delete_macros(request, macros_id):
    macros = get_object_or_404(Macros, id=macros_id, user=request.user)
    if request.method == "POST":
        macros.delete()
        return redirect(reverse('mealPlannerApp:macros'))
    return redirect(reverse('mealPlannerApp:macros'))

@login_required
def food_view(request):
    return render(request, 'mealPlannerApp/food.html')

@login_required
def plan_view(request):
    return render(request, 'mealPlannerApp/plan.html')