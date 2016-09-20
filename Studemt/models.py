from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class Student(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    category_choice = (('sc', 'S.C'), ('gen', 'General'), ('st', 'S.T'), ('obc-a', 'O.B.C-A'), ('obc-b', 'O.B.C-B'),)
    guardian_name = models.CharField(max_length=255)
    dob = models.DateField()
    address = models.TextField()
    category = models.CharField(max_length=255, choices=category_choice)
    domcile_wb = models.BooleanField()
    contact_number = models.IntegerField()
    email = models.EmailField(max_length=255)
    rank = models.IntegerField()
    year_of_passing = models.IntegerField()

    def __str__(self):
        return self.student.username + '-->' + self.email


class Subject(models.Model):
    stream = models.CharField(max_length=255)
    availability = models.IntegerField()

    def __str__(self):
        return str(self.id) + '. ' + self.stream + " --> " + str(self.availability)


class Hello(models.Model):
    serial = models.IntegerField()
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    first_pref = models.ForeignKey(Subject, related_name='first')
    second_pref = models.ForeignKey(Subject, related_name='second', null=True, blank=True)
    third_pref = models.ForeignKey(Subject, related_name='third', null=True, blank=True)
    fourth_pref = models.ForeignKey(Subject, related_name='fourth', null=True, blank=True)
    date_time = models.DateTimeField()

    def __str__(self):
        return self.student.get_full_name() + ' || ' + self.student.username
