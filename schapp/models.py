from django.db import models
from django.shortcuts import reverse


# Create your models here.
DEPARTMENT = (
    ('english', 'English'),
    ('maths', 'Maths'),
    ('swahili', 'Swahili'),
    ('Biology', 'Biology'),
    ('Chemistry', 'Chemistry'),
    ('Physics', 'Physics'),
    ('Humanities', 'Humanities'),
    ('Grp4/5', 'Grp4/5'),
)

CLASS = (
    ('form 1', 'Form 1'),
    ('form 2', 'Form 2'),
    ('form 3', 'Form 3'),
    ('form 4', 'Form 4'),
)

YEAR = (
    ('2018', '2018'),
    ('2019', '2019'),
    ('2020', '2020'),
    ('2021', '2021'),
    ('2022', '2022'),
    ('2023', '2023'),

)


class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    admission = models.BigIntegerField(unique=True)
    form = models.CharField(choices=CLASS, default='Form 1', max_length=6)
    house = models.CharField(max_length=50)
    club = models.CharField(max_length=50)
    #passport = models.ImageField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('schapp:teacher-index')


class Term(models.Model):
    name = models.CharField(max_length=10, unique=True)
    year = models.CharField(choices=YEAR, max_length=6, default=2018)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=50)
    department = models.CharField(choices=DEPARTMENT, max_length=45, default='Maths')

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=20, unique=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT)
    department = models.CharField(choices=DEPARTMENT, max_length=45, default='Maths')

    def __str__(self):
        return self.name


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    form = models.CharField(choices=CLASS, max_length=6, default='form 1')
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    cat = models.CharField(max_length=2)
    exam = models.CharField(max_length=3)
    remark = models.CharField(max_length=50)

    def __str__(self):
        return self.subject.name



