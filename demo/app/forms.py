from django import forms

class user_form(forms.Form):
    roll_number=forms.IntegerField()
    name=forms.CharField()
    age=forms.IntegerField()
    email=forms.EmailField()