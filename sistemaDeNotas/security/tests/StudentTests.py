from django.test import TestCase
from security.models.Person import Person


class StudentTestCase(TestCase):
    def setUp(self):
        Person.objects.create(id=1, first_name="Juan", last_name="Perez", identifier="45876678", gender="M")
        Person.objects.create(id=2, first_name="Ana", last_name="Sanchez", identifier="45543789", gender="F")

    def test_course(self):
        alumna = Person.objects.get(first_name="Ana")
        alumno = Person.objects.get(first_name="Juan")
        self.assertEqual(alumna.gender, 'F')
        self.assertEqual(alumno.gender, 'M')
