from django import forms
from security.models import Person


class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = ('identifier', 'first_name', 'last_name')

