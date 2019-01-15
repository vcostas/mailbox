#!/usr/bin/env python
# -*- coding: utf-8 -*-
from assignment.services.StudentAssignmentService import StudentAssignmentService
from core.services.ServiceBase import ServiceBase
from security.models.Responsible import Responsible


class ResponsibleService(ServiceBase):
    studentAssignmentService = StudentAssignmentService()

    def __init__(self):
        super(ResponsibleService, self).__addModel__(Responsible())

    def get_responsible(self, person):
        return self.MODEL.__class__.objects.filter(responsible=person, is_responsible=True).order_by(
            'student__last_name', 'student__first_name').all()

    def get_responsible_active(self, person):
        resp = self.get_responsible(person)
        result = []
        for r in resp:
            st = self.studentAssignmentService.get_assignment_active(st.student)
            if len(st) > 0:
                result.append(r)
        return result

    def get_responsible_by_student_qs(self, person):
        return self.MODEL.__class__.objects.filter(student=person)\
                 .order_by('relationship__name', 'responsible__last_name', 'responsible__first_name')

    def get_responsible_by_student(self, person):
        return self.get_responsible_by_student_qs(person).all()
