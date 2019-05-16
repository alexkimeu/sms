from django.shortcuts import render, get_object_or_404
from ..forms import StudentForm
from ..models import Student
from django.http import JsonResponse
from django.template.loader import render_to_string


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
        form = StudentForm(request.POST or None, request.FILES or None)
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
