from django.forms import forms, fields, PasswordInput, ModelForm, TextInput

from .models import Site


# validation of data

# agregarle a todos los field un widget en los atributos
class BootstrapMixin():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = field.widget.attrs.get('class', '')
            field.widget.attrs['class'] += ' form-control'


class RegistrationForm(BootstrapMixin, forms.Form):
    # estos attrs son para agregar los tributos de bootstraps al from
    email = fields.EmailField()
    # para que no se vea la clave
    # nombre para los labels
    password = fields.CharField(label="Password",
                                widget=PasswordInput())
    password2 = fields.CharField(label='Repeat Password', widget=PasswordInput())
    avatar = fields.ImageField()

    def clean(self):
        # mis propias validaciones
        cleaned_data = super(RegistrationForm, self).clean()
        if cleaned_data['password'] != cleaned_data['password2']:
            # para no poner el error en un titulo en concreto
            self.add_error(None, 'password not equals')
        return cleaned_data


class LoginForm(BootstrapMixin, forms.Form):
    email = fields.EmailField()
    password = fields.CharField(
        label="Password",
        widget=PasswordInput())


class SiteForm(BootstrapMixin, ModelForm):
    class Meta:
        model = Site
        fields = ('url', 'name')
