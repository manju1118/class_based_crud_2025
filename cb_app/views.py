from django.shortcuts import render,redirect
from .models import Student
from .forms import StudentForm


def index(request):
    """Render the index page with a list of students."""
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'cb_app/index.html',context)

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = StudentForm()
    context =  {'form': form}
    return render(request, 'cb_app/student_create.html',context)
def student_details(request, student_id):
    student = Student.objects.get(id=student_id)
    context = {
        'student':student
    }
    return render(request, 'cb_app/student_details.html',context)

def student_update(request,student_id):
    student = Student.objects.get(id=student_id)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance = student)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form,
        'student': student
    }
    return render(request, 'cb_app/student_create.html', context)

def student_delete(request,student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return redirect('index')