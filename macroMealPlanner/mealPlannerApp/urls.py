from django.urls import path
from mealPlannerApp import views

app_name = "mealPlannerApp"

urlpatterns = [
    path('', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('macros/', views.macros_view, name='macros'),
    path('food/', views.food_view, name='food'),
    path('plan/', views.plan_view, name='plan'),
    path('delete_macros/<int:macros_id>', views.delete_macros, name='delete_macros')
]