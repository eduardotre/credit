from django import forms

from .models import Application


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        exclude = ('owner',)
        fields = ['first_name', 'last_name', 'business', 'm_number', 'email']
        labels = {'first_name': 'Nombre', 'last_name': 'Apellidos',
                  'business': 'Employer', 'm_number': 'Numero Telefonico',
                  'email': 'Correo Electronico'}
