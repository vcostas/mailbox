#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth.models import Group
from django.template.defaulttags import register


@register.filter(name='has_group')
def has_group(user, group_name):
    group = Group.objects.get(name=group_name)
    return group in user.groups.all()