from django.db import models
from django.shortcuts import reverse


# Create your models here.
CLASS = (
    ('form 1', 'Form 1'),
    ('form 2', 'Form 2'),
    ('form 3', 'Form 3'),
    ('form 4', 'Form 4'),
)


class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    admission = models.BigIntegerField(primary_key=True)
    form = models.CharField(choices=CLASS, default='Form 1', max_length=6)
    house = models.CharField(max_length=50)
    club = models.CharField(max_length=50)
    #passport = models.ImageField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('schapp:teacher-index')




