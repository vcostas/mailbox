#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth.models import Group
from core.services.ServiceBase import ServiceBase
from guardian.shortcuts import get_objects_for_user, Permission
from core.services.SubjectService import SubjectService


class SecurityService(ServiceBase):
    subjectService = SubjectService()

    def __init__(self):
        self.subjectService = SubjectService()


    def checkpermOnsubject(self,user,subject,codename):
        #si es supervisor puede
        group = Group.objects.get(name='Administrador del Sistema')

        if group in user.groups.all():
            return True
        #chequeo si la materia es del docente
        user_subjects = self.subjectService.getSubjects_by_User(user)
        # si la materia es del docente y tiene el proemiso global retorno ok
        if subject in user_subjects and user.has_perm('core.'+ codename):
            return True

        user_subjects_with_perms = self.subjectService.getSubjects_by_User_Perm(user,Permission.objects.get_by_natural_key(codename,'core','Subject'))
        # si no es del docente chequeo si tiene el permiso asignado

        if subject in user_subjects_with_perms:
            return True

        return False

    def checkpermOncourse(self, user, course, codename):
        # si es supervisor puede
        group = Group.objects.get(name='Administrador del Sistema')

        if group in user.groups.all():
            return True

        # chequeo si tiene el permiso asignado particularmente
        user_courses_with_perms = get_objects_for_user(user, 'core.'+codename,accept_global_perms=False)

        if course in user_courses_with_perms:
            return True

    def checkpermOnperson(self,user,subject,codename):
        return NotImplementedError


    def checkpermOneducationalService(self,user,educationalService,codename):
        # si es supervisor puede
        group = Group.objects.get(name='Administrador del Sistema')

        if group in user.groups.all():
            return True

        # chequeo si tiene el permiso asignado particularmente
        user_es_with_perms = get_objects_for_user(user,perms= 'core.'+codename,accept_global_perms=False)
        if educationalService in user_es_with_perms:
            return True