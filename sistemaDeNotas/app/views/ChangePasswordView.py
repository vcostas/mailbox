#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import View
from security.forms.ChangePasswordForm import ChangePasswordForm


class ChangePasswordView(View):
    @method_decorator(login_required)
    def get(self, request):
        form = ChangePasswordForm()
        return render(request, 'change_password.html', {'form': form})

    @method_decorator(login_required)
    def post(self, request):
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            new_password = request.POST['password_1']
            user_logged = User.objects.get(username=request.user.username)
            user_logged.set_password(new_password)
            user_logged.save()
            update_session_auth_hash(request, user_logged)
            return redirect('/index')
        else:
            return render(request, 'change_password.html', {'form': form})