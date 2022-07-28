from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import FormView, CreateView, DetailView, UpdateView, ListView

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
        # reques.Files para cargar archivos
        form = RegistrationForm(request.POST, request.FILES)
        context['form'] = form
        if form.is_valid():
            # cleaned_data es la data limpia y validada
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            avatar = form.cleaned_data['avatar']
            # servico para guardar el user en bd
            register_user(email, password, avatar)
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
class SiteView(LoginRequiredMixin, CreateView):
    template_name = 'web/sites/edit.html'
    form_class = SiteForm
    # con reverse_lazy buscamos el url por el nombre en el url.py haciendo un scan
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super(SiteView, self).form_valid(form)


class SiteDetailView(LoginRequiredMixin, DetailView):
    model = Site
    template_name = 'web/sites/detail.html'


class SiteUpdateView(LoginRequiredMixin, UpdateView):
    model = Site
    template_name = 'web/sites/edit.html'
    fields = ('name', 'url')

    def get_success_url(self):
        # asi para meterle el id
        return reverse('site', args=(self.object.id,))


class SiteListView(LoginRequiredMixin, ListView):
    paginate_by = 10
    model = Site
    template_name = 'web/sites/list.html'


def html_view(request):
    return render(request, 'web/html.html')
