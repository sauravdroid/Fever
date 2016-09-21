from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class Student(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    category_choice = (('sc', 'S.C'), ('gen', 'General'), ('st', 'S.T'), ('obc-a', 'O.B.C-A'), ('obc-b', 'O.B.C-B'),)
    guardian_name = models.CharField(max_length=255,blank=False)
    dob = models.DateField(blank=False)
    address = models.TextField(blank=False)
    category = models.CharField(max_length=255, choices=category_choice,blank=False)
    domcile_wb = models.BooleanField(blank=False)
    contact_number = models.IntegerField(blank=False)
    email = models.EmailField(max_length=255,blank=False)
    rank = models.IntegerField(blank=False,unique=True)
    year_of_passing = models.IntegerField(blank=False)
    #REQUIRED_FIELDS = ['guardian_name',]

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
    first_pref = models.ForeignKey(Subject, related_name='first', null=True)
    second_pref = models.ForeignKey(Subject, related_name='second', null=True, blank=True)
    third_pref = models.ForeignKey(Subject, related_name='third', null=True, blank=True)
    fourth_pref = models.ForeignKey(Subject, related_name='fourth', null=True, blank=True)
    date_time = models.DateTimeField()


    class Meta:
        verbose_name_plural = 'Student Preference'
    def __str__(self):
        return self.student.get_full_name() + ' || ' + self.student.username
