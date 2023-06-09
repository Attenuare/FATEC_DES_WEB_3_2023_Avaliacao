from django.db import models
from .enums import * 


class StudentPresence(models.Model):
	students_name = models.CharField('student_name', max_length=150)
	teachers_name = models.IntegerField('teachers_name')
	semester = models.IntegerField('semester', choices=POSSIBLESEMESTERS)
