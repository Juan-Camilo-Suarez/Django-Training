from django.forms import forms, fields, PasswordInput, ModelForm, TextInput

from .models import Site


# validation of data


class RegistrationForm(forms.Form):
    # estos attrs son para agregar los tributos de bootstraps al from
    email = fields.EmailField(widget=TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email'
    }))
    # para que no se vea la clave
    # nombre para los labels
    password = fields.CharField(label="Password",
                                widget=PasswordInput(attrs={'class': 'form-control',
                                                            'placeholder': 'password'}))
    password2 = fields.CharField(label='Repeat Password', widget=PasswordInput(attrs={'class': 'form-control',
                                                                                      'placeholder': 'password'}))
    avatar = fields.ImageField()

    def clean(self):
        # mis propias validaciones
        cleaned_data = super(RegistrationForm, self).clean()
        if cleaned_data['password'] != cleaned_data['password2']:
            # para no poner el error en un titulo en concreto
            self.add_error(None, 'password not equals')
        return cleaned_data


class LoginForm(forms.Form):
    email = fields.EmailField()
    password = fields.CharField(
        label="Password",
        widget=PasswordInput())


class SiteForm(ModelForm):
    class Meta:
        model = Site
        fields = ('url', 'name')
