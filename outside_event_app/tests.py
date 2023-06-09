from .forms import StudentPresenceForm
from .models import StudentPresence
from django.test import TestCase


class HomeTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/')

    def test_200_response(self):
        self.assertEqual(self.response.status_code, 200)

    def test_text(self):
        self.assertContains(self.response, 'Registrar Presença')

    def test_templates_home(self):
        self.assertTemplateUsed(self.response, 'registration.html')


class RegistrationTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/listar')

    def test_200_response(self):
        self.assertEqual(self.response.status_code, 200)

    def test_text(self):
        self.assertContains(self.response, 'presente')


    def test_templates_home(self):
        self.assertTemplateUsed(self.response, 'registration_presence.html')

class StudentPresentTest(TestCase):
    def setUp(self):
        student_1 = {
            'students_name': 'Roberto Santos',
            'teachers_name': 1,
            'semester': 2
        }
        student_2 = {
            'students_name': None,
            'teachers_name': 2,
            'semester': 2
        }
        self.student_presence = StudentPresenceForm(student_1)
        self.student_presence_fail = StudentPresenceForm(student_2)
        self.student_presence.is_valid()
        self.student_presence_db = StudentPresence(**self.student_presence.cleaned_data)

    def test_student_registrationform(self):
        self.assertTrue(self.student_presence.is_valid())

    def test_form_fields(self):
        self.student_presence.is_valid()
        self.assertEqual(self.student_presence.cleaned_data.get('students_name'), 'Roberto Santos')
        self.assertEqual(self.student_presence.cleaned_data.get('teachers_name'), '1')
        self.assertEqual(self.student_presence.cleaned_data.get('semester'), '2')

    def test_emppty_field(self):
        self.assertFalse(self.student_presence_fail.is_valid())

    def test_ocjects_type(self):
        self.assertIs(type(self.student_presence), StudentPresenceForm)
        self.assertIs(type(self.student_presence_db), StudentPresence)

    def test_database_occurrence(self):
        self.student_presence_db.save()
        db_occurrence = StudentPresence.objects.get(pk=1)
        self.assertEqual(db_occurrence.students_name, self.student_presence.cleaned_data.get('students_name'))
        self.assertEqual(str(db_occurrence.teachers_name), self.student_presence.cleaned_data.get('teachers_name'))
        self.assertEqual(str(db_occurrence.semester), self.student_presence.cleaned_data.get('semester'))

    def test_view_get_choices_response(self):
        self.test_database_occurrence()
        self.response = self.client.get('/')
        self.assertEqual(self.response.status_code, 200)

    def test_view_get_choices_semester(self):
        self.test_view_get_choices_response()
        self.response = self.client.get('/')
        self.assertContains(self.response, '2 Semestre')

    def test_view_get_choices_teacher(self):
        self.test_view_get_choices_response()
        self.response = self.client.get('/')
        self.assertContains(self.response, 'Orlando')
