#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models


class IdentifierType(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    name = models.CharField(unique=True, max_length=50, verbose_name='Relacion', null=False)
    description = models.CharField(max_length=255, verbose_name='Descripcion', null=False)

    class Meta:
        verbose_name = 'Tipo de documento'
        verbose_name_plural = 'Tipos de documentos'
        app_label = 'security'
