#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    force_password_change = models.BooleanField(default=True)

    def __unicode__(self):
        return u"%s" % self.user

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
        app_label = 'security'
