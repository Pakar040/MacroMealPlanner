from typing import Any
from django import forms
from django.contrib.auth.models import User
from .models import Macros, Food

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

    def save(self, commit: bool = True) -> Any:
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
    

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class MacrosForm(forms.ModelForm):
    class Meta:
        model = Macros
        fields = ['name', 'protein', 'fat', 'carbs']


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'units', 'amount', 'protein', 'fat', 'carbs']


class MacroMealPlanForm(forms.Form):

    foods = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )

    macros = forms.ChoiceField(
        required=True,
    )

    def __init__(self, user, *args, **kwargs) -> None:
        super(MacroMealPlanForm, self).__init__(*args, **kwargs)
        self.fields['foods'].choices = [(food.id, food.name) for food in Food.objects.filter(user=user)]
        self.fields['macros'].choices = [(macros.id, macros.name) for macros in Macros.objects.filter(user=user)]

        self.fields['foods'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['macros'].widget.attrs.update({'class': 'form-control custom-dropdown'})
