#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth.models import User

from core.services.ServiceBase import ServiceBase
from guardian.shortcuts import get_objects_for_user


class UserService(ServiceBase):

    def __init__(self):
        super(UserService, self).__addModel__(User())

    def get_profesor_materia(self,materia):
        # Retorna el profesor/a de una determinada materia
        #return User.objects.filter(materia__usuarios__materia=materia)[0]
        return User.objects.filter(subject__users__subject=materia)[0]


