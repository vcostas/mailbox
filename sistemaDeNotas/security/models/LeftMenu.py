#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth.models import Permission
from django.db import models


class LeftMenu(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    parent = models.BigIntegerField(10, null=True)
    depth = models.IntegerField(default=0, null=False)
    path = models.CharField(max_length=255, null=True)
    order = models.IntegerField(default=0, null=False)
    text = models.CharField(max_length=255, default='', null=False)
    url = models.CharField(max_length=255, default='', null=False)
    codename = models.CharField(max_length=30, unique=True)
    icon = models.CharField(max_length=255, null=True)
    perm = models.ForeignKey(Permission,verbose_name='Permission',null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Item de menu'
        verbose_name_plural = 'Items de menu'
        app_label = 'security'
        permissions = (("ver_item_menu", "Ver item menu"),
                       )
