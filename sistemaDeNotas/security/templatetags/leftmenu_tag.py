#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import template
import json

from security.services.MenuService import MenuService

register = template.Library()


@register.simple_tag(takes_context=True)
def get_leftmenu_jsontree(context):
    #loggedUser = context['user']
    #loggedUser.id
    menuService = MenuService();
    menuFromSecurity = menuService.get_leftmenu_for_user(context['user'])
    return json.dumps(menuFromSecurity)
