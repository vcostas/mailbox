#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from security.models.Person import Person
from security.models.ResponsibleType import ResponsibleType


class Responsible(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    student = models.ForeignKey(Person, verbose_name='Alumno', on_delete=None, related_name='student')
    responsible = models.ForeignKey(Person, verbose_name='Responsable', on_delete=models.CASCADE, related_name='responsible')

    is_responsible = models.BooleanField(default=False, verbose_name='Es responsable legal')
    relationship = models.ForeignKey(ResponsibleType, verbose_name='Relacion', null=False, on_delete=None)
    start_date = models.DateField(verbose_name='Fecha inicio vigencia', auto_now_add=True)
    end_date = models.DateField(null=True, verbose_name='Fecha fin vigencia')

    class Meta:
        verbose_name = 'Relacion responsable alumno'
        verbose_name_plural = 'Relacion responsables alumno'
        app_label = 'security'
