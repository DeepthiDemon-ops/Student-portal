from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
from django.shortcuts import render, redirect, get_object_or_404

def home(request):

    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')

    form = StudentForm()

    students = Student.objects.all()

    return render(
        request,
        'home.html',
        {
            'form': form,
            'students': students
        }
    )

def delete_student(request, id):

    student = Student.objects.get(id=id)

    student.delete()

    return redirect('/')
def edit_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.name = request.POST['name']
        student.roll_no = request.POST['roll_no']
        student.save()
        return redirect('/')

    return render(request, 'edit.html', {'student': student})
