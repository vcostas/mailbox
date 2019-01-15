#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth.models import Group

from core.services.ServiceBase import ServiceBase


class GroupService(ServiceBase):

    def __init__(self):
        super(GroupService, self).__addModel__(Group())


