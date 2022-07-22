from django.forms import forms, fields


# validation of data

class RegistrationForm(forms.Form):
    email = fields.EmailField()
    password = fields.CharField()
    password2 = fields.CharField()

    def clean(self):
        # mis propias validaciones
        cleaned_data = super(RegistrationForm, self).clean()
        if cleaned_data['password'] != cleaned_data['password2']:
            self.add_error('password', 'password not correct')
        return cleaned_data
