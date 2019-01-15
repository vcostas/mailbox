#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.generic import View

from security.forms.LoginForm import LoginForm


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            form = LoginForm()
            instance = 'fameghino'
            login_title = 'Florentino Ameghino'
            url_logo = '/static/images/logo3.png'
            return render(request, 'login.html', {'form': form, 'login_title': login_title, 'url_logo': url_logo})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=User.objects.get(username=request.POST['username']),
                                password=request.POST['password'])
            login(request, user)
            next = request.GET['next'] if 'next' in request.GET else 'index'
            return redirect(next)
        else:
            instance = 'fameghino'
            login_title = 'Florentino Ameghino'
            url_logo = '/static/images/logo3.png'
            return render(request, 'login.html', {'form': form, 'login_title': login_title, 'url_logo': url_logo})