from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from .forms import RegistrationForm, LoginForm, SiteForm
from .models import Site
from .services import register_user


def main_view(request):
    return render(request, 'web/main.html')


def register_view(request):
    context = {'form': RegistrationForm()}
    # recoger toda la informacion del post
    # print(request.POST)
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        context['form'] = form
        if form.is_valid():
            # cleaned_data es la data limpia y validada
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # servico para guardar el user en bd
            register_user(email, password)
            context['message'] = 'registration success'
    return render(request, 'web/registration.html', context)


def login_view(request):
    form = LoginForm()
    context = {'form': form}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # debemos probar que los datos ingresados son correctos
            # login()revisa que los datos del login este en bd
            # authenticate() imformacion de la session y del usuario authenticado y revisa que los datos sean corretos
            user = authenticate(request, email=email, password=password)
            if user is None:
                # context['error'] = 'Email or password incorrect'
                form.add_error(None, "email or password incorrect")
                context['form'] = form
            else:
                login(request, user)
                return redirect('main')
    return render(request, 'web/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('main')

# LoginRequiredMixin para ver si esta autorizado el user
class SiteView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'web/sites/add.html', {'form': SiteForm()})

    def post(self, request, *args, **kwargs):
        form = SiteForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            data['user_id'] = request.user.id
            Site.objects.create(**data)
        context = {'form': form}
        return render(request, 'web/sites/add.html', context)
