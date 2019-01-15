#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from datetime import date


class Student(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    first_name = models.CharField(max_length=64, verbose_name='Nombre')
    last_name = models.CharField(max_length=64, verbose_name='Apellido')
    identifier = models.CharField(max_length=64, verbose_name='DNI')
    gender = models.CharField(max_length=1, verbose_name='Genero', null=True)
    birthdate = models.DateField(verbose_name='Fecha Nacimiento', blank=True, null=True)

    user = models.OneToOneField(User, on_delete=None, null=True)

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name

    def nombre_formateado(self):
        return u'%s, %s' % (self.last_name, self.first_name)

    def is_birthday(self):
        today = date.today()
        return self.birthdate.day == 10 and self.birthdate.month == 10

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        app_label = 'security'
        permissions = (("view_birthday", "Ver cumpleaños"),
                       )