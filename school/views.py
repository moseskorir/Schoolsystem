from django.shortcuts import render, redirect

from .forms import StudentForm
from .models import Student


def students(request):
    students = Student.objects.all()
    context = {
        "students": students
    }
    return render(request, "school/students.html", context=context)


def student_form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = StudentForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return redirect('students')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = StudentForm()

    return render(request, 'school/student_form.html', {'form': form})
