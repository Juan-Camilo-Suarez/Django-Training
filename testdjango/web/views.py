from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from .forms import RegistrationForm
from .models import User


def main_view(request):
    return render(request, 'web/main.html')


def register_view(request):
    # recoger toda la informacion del post
    # print(request.POST)
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if not form.is_valid():
            return render(request, 'web/registration.html', {
                'form': form
            })
        email = request.POST['email']
        password = request.POST['password']
        user = User(email=email)
        user.set_password(password)
        user.save()
        return redirect('main')
    return render(request, 'web/registration.html')
