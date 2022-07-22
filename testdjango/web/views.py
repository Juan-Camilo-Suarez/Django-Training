from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from .models import User


def main_view(request):
    return render(request, 'web/main.html')


def register_view(request):
    # recoger toda la informacion del post
    # print(request.POST)
    if request.method == 'POST':
        if request.POST['password'] != request.POST['password2']:
            return HttpResponse("password are not equal")
        email = request.POST['email']
        password = request.POST['password']
        user = User(email=email)
        user.set_password(password)
        user.save()
        return redirect('main')
    return render(request, 'web/registration.html')
