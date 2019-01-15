#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic import View


class LogOutView(View):
    @method_decorator(login_required)
    def get(self, request):
        logout(request)
        return redirect('login')