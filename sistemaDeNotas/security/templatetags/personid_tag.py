#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import template
from security.models import Person

register = template.Library()


@register.simple_tag(takes_context=True)
def get_personid(context):
    loggedUser = context['user']
    loggedPerson = Person.objects.get(user__username=loggedUser)
    return loggedPerson.id
