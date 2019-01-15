#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import View
from core.services.AssignmentService import AssignmentService


class StudentView(View):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        assignments = AssignmentService().get_assignment_to_educationalservice()
        students = map(lambda a: a.student, assignments)
        return render(request, 'students.html',{'assignments': assignments })