from django.urls import path
from .views import teachers

app_name = 'schapp'

urlpatterns = [
    path('form1', teachers.form1_students, name='form1'),
    path('form2', teachers.form2_students, name='form2'),
    path('form3', teachers.form3_students, name='form3'),
    path('form4', teachers.form4_students, name='form4'),
    path('add-student', teachers.add_student, name='add-student'),
    path('(?P<pk>\d+)/student-update/', teachers.update_student, name='update-student'),
    path('(?P<pk>\d+)/student-delete/', teachers.delete_student, name='delete-student'),
]
