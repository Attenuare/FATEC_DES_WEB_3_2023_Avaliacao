from django import forms
from .enums import * 


class StudentPresenceForm(forms.Form):
    students_name = forms.CharField(label='Nome Estudante', max_length=150)
    teachers_name = forms.ChoiceField(label='Professor', choices=POSSIBLETEACHERS)
    semester = forms.ChoiceField(label='Semestre', choices=POSSIBLESEMESTERS)

    def clean_students_name(self):
        students_name = self.cleaned_data['students_name']
        return students_name
    
    def clean_teachers_name(self):
        teachers_name = self.cleaned_data['teachers_name']
        return teachers_name
    
    def clean_semester(self):
        semester = self.cleaned_data['semester']
        return semester

    def clean(self):
        self.cleaned_data = super().clean()
        return self.cleaned_data
