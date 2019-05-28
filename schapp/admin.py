from django.contrib import admin
from .models import Student, Grade, Term, Subject, Teacher


# Register your models here.
admin.site.register(Student)
admin.site.register(Grade)
admin.site.register(Term)
admin.site.register(Teacher)
admin.site.register(Subject)

