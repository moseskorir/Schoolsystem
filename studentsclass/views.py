from django.shortcuts import render, redirect
from .forms import SubjectsForm
from .models import Subjects


def subjects(request):
    subjects = Subjects.objects.all()
    context = {
        "subjects": subjects
    }
    return render(request, 'studentsclass/subjects.html', context=context)

def subjects_form(request):
    if request.method == 'POST':
        form = SubjectsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subjects')

    else:
        form = SubjectsForm()

    return render(request, 'studentsclass/subjects_form.html', {'form':form})

