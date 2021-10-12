from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=20, min_length=6)
    remember = forms.IntegerField(required=False)
