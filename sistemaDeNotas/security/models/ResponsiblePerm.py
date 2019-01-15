#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from security.models.Responsible import Responsible


class ResponsiblePerm(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    responsible = models.ForeignKey(Responsible, null=False, verbose_name='Responsable', on_delete=models.CASCADE)
    has_perm = models.BooleanField(default=True, null=False, verbose_name='Tiene permiso')

    class Meta:
        verbose_name = 'Permiso responsable'
        verbose_name_plural = 'Permisos responsables'
        app_label = 'security'
