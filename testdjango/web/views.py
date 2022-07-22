from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from .forms import RegistrationForm
from .models import User
from .services import register_user


def main_view(request):
    return render(request, 'web/main.html')


def register_view(request):
    context = {}
    # recoger toda la informacion del post
    # print(request.POST)
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if not form.is_valid():
            context['form'] = form
        else:
            # cleaned_data es la data limpia y validada
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # servico para guardar el user en bd
            register_user(email, password)
            context['message'] = 'registration success'
    return render(request, 'web/registration.html', context)
