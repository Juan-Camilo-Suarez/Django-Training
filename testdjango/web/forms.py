from django.forms import forms, fields, PasswordInput


# validation of data

class RegistrationForm(forms.Form):
    email = fields.EmailField()
    #para que no se vea la clave
    #nombre para los labels
    password = fields.CharField(label="Password", widget=PasswordInput())
    password2 = fields.CharField(label='Repeat Password', widget=PasswordInput())

    def clean(self):
        # mis propias validaciones
        cleaned_data = super(RegistrationForm, self).clean()
        if cleaned_data['password'] != cleaned_data['password2']:
            self.add_error('password', 'password not correct')
        return cleaned_data
