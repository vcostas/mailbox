#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.template.defaulttags import register


@register.filter(name='has_perm')
def has_perm(user, codename):
    # group =  Group.objects.get(name=group_name)
    return user.has_perm(codename);