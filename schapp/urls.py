from django.urls import path
from .views import teachers, students

app_name = 'schapp'

urlpatterns = [
    # Teacher psths
    path('students', teachers.StudentListView.as_view(), name='all-students'),
    path('form1', teachers.form1_students, name='form1'),
    path('form2', teachers.form2_students, name='form2'),
    path('form3', teachers.form3_students, name='form3'),
    path('form4', teachers.form4_students, name='form4'),
    path('(?P<pk>\d+)/', teachers.student_detail, name='student-detail'),
    path('add-student', teachers.add_student, name='add-student'),
    path('(?P<pk>\d+)/student-update/', teachers.update_student, name='update-student'),
    path('(?P<pk>\d+)/student-delete/', teachers.delete_student, name='delete-student'),
    path('(?P<pk>\d+)/add-grade', teachers.add_grade, name='add-grade'),

    # Student paths
    path('profile', students.student_profile, name='student-profile'),
]


