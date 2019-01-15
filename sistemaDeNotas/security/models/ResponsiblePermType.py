#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django_mysql.models import JSONField


class ResponsiblePermType(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    name = models.CharField(unique=True, max_length=50, verbose_name='Permiso', null=False)
    description = models.CharField(max_length=255, verbose_name='Descripcion', null=False)
    perms = JSONField(default=None)

    class Meta:
        verbose_name = 'Tipo de Permiso responsable'
        verbose_name_plural = 'Tipos de Permisos responsables'
        app_label = 'security'
