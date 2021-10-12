from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, reverse
from .forms import LoginForm
from django.http import HttpResponse


def login_view(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        remember = form.cleaned_data.get('remember')
        user = authenticate(request, username=email, password=password)
        if user:
            if user.is_active:
                login(request, user)
                if remember:
                    request.session.set_expiry(None)
                else:
                    request.session.set_expiry(0)
                return HttpResponse("success")
            else:
                return HttpResponse("user is not active")
        else:
            return HttpResponse("email or password not match")
    else:
        return HttpResponse("error")


def logout_view(request):
    logout(request)
    return redirect(reverse('top'))
