from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import StudentPresenceForm
from .models import StudentPresence
from .enums import *


def index(request):
    student_presence = StudentPresenceForm(request.POST)
    context = {'student_presence': student_presence}
    if student_presence.is_valid():
        if request.method == 'POST':
            student_registration = StudentPresence(**student_presence.cleaned_data)
            student_registration.save()
            return redirect('index')
        else:
            return render(request, 'registration.html')
    else:
        return render(request, 'registration.html', context)

def presences(request):
    all_presences = StudentPresence.objects.all()
    temp_list = list()
    for occurrence in all_presences:
        unique_occurrence = {
            'students_name': occurrence.students_name,
            'teachers_name': POSSIBLETEACHERS[occurrence.teachers_name - 1][1],
            'semester': POSSIBLESEMESTERS[occurrence.semester - 1][1]
        }
        temp_list.append(unique_occurrence)
    all_presences = temp_list
    return render(request, 'registration_presence.html', {'all_presences': all_presences})
