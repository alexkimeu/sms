from django.shortcuts import render, get_object_or_404
from ..forms import StudentForm, GradeForm
from ..models import Student, Subject
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.generic import ListView


class StudentListView(ListView):
    model = Student
    template_name = 'schapp/teachers/index.html'
    ordering = 'form'
    context_object_name = 'students'


def form1_students(request):
    students = Student.objects.filter(form='form 1')
    return render(request, 'schapp/teachers/index.html', {'students': students})


def form2_students(request):
    students = Student.objects.filter(form='form 2')
    return render(request, 'schapp/teachers/index.html', {'students': students})


def form3_students(request):
    students = Student.objects.filter(form='form 3')
    return render(request, 'schapp/teachers/index.html', {'students': students})


def form4_students(request):
    students = Student.objects.filter(form='form 4')
    return render(request, 'schapp/teachers/index.html', {'students': students})


# Saves student to DB
def save_student_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            students = Student.objects.filter(form='form 1')
            data['html_student_list'] = render_to_string('schapp/teachers/includes/partial-student-list.html',
                                                         {'students': students})
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


# Partial to re-use
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
    else:
        form = StudentForm()
    return save_student_form(request, form, 'schapp/teachers/includes/partial-student-add.html')


def update_student(request, pk):
    s = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=s)
    else:
        form = StudentForm(instance=s)
    return save_student_form(request, form, 'schapp/teachers/includes/partial-student-update.html')


def delete_student(request, pk):
    s = get_object_or_404(Student, pk=pk)
    data = dict()
    if request.method == 'POST':
        s.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        students = Student.objects.filter(form='form 1')
        data['html_student_list'] = render_to_string('schapp/teachers/includes/partial-student-list.html', {
            'students': students
        })
    else:
        context = {'s': s}
        data['html_form'] = render_to_string('schapp/teachers/includes/partial-student-delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


def save_grade_form(request, form, template_name, student):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            grade = form.save(commit=False)
            grade.student = student
            grade.save()
            data['form_is_valid'] = True
            students = Student.objects.all()
            data['html_student_list'] = render_to_string('schapp/teachers/includes/partial-student-list.html',
                                                         {'students': students})
        else:
            data['form_is_valid'] = False
    context = {'form': form, 'student': student}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def add_grade(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = GradeForm(request.POST)
    else:
        form = GradeForm(instance=student.grade_set.first())
    return save_grade_form(request, form, 'schapp/teachers/includes/partial-grade-add.html', student)


"""
def add_grade(request, pk):
    student = get_object_or_404(Student, pk=pk)
    data = dict()
    if request.method == 'POST':
        form = GradeForm(request.POST or None)
        if form.is_valid():
            grade = form.save(commit=False)
            grade.student = student
            grade.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        form = GradeForm()
    context = {'form': form, 'student': student}
    data['html_form'] = render_to_string('schapp/teachers/includes/partial-grade-add.html',
                                         context, request=request)
    return JsonResponse(data)
"""


def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    subjects = Subject.objects.all()
    return render(request, 'schapp/teachers/student-details.html', {'student': student, 'subjects': subjects})
