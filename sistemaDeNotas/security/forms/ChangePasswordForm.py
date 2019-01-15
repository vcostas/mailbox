#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms


class ChangePasswordForm(forms.Form):
    password_1 = forms.CharField(label='Clave 1', widget=forms.PasswordInput, max_length=64)
    password_2 = forms.CharField(label='Clave 2', widget=forms.PasswordInput, max_length=64)

    def clean(self):
        password_1 = self.cleaned_data.get('password_1')
        password_2 = self.cleaned_data.get('password_2')
        if password_1 != password_2:
            raise forms.ValidationError('No coinciden las contraseñas')
        return password_1


    def is_valid(self):
        valid = super(ChangePasswordForm, self).is_valid()
        if not valid:
            return valid
        return True