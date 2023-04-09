from django.db import models

# Create your models here.

branches = (('ME','ME'), ('CSE','CSE'), ('ECE','ECE'), ('CHE','CHE'), ('CE','CE'), ('MME','MME'))
Fbranches = (('ME','ME'), ('CSE','CSE'), ('ECE','ECE'), ('CHE','CHE'), ('CE','CE'), ('MME','MME'), ('NA','NA'))
year = (('E1','E1'),('E2','E2'), ('E3','E3'), ('E4','E4'))

class Class(models.Model):
    branch = models.CharField(choices=branches, max_length=5, default='ME')
    year = models.CharField(choices=year, max_length=5, default='E4')
    classname = models.CharField(max_length=10)

    def __str__(self):
        return self.classname


class Faculty(models.Model):
    facultyName = models.CharField(max_length=50)
    dept = models.CharField(choices=Fbranches, max_length=5, default='NA')
    position = models.CharField(max_length=20, default='Assistant Faculty')

    def __str__(self):
        return self.facultyName


class Student(models.Model):
    classname = models.ForeignKey(Class, on_delete=models.CASCADE)
    stud_name = models.CharField(max_length=50)
    idnum = models.CharField(max_length=10)
    email = models.EmailField()
    cgpa = models.FloatField()

    def __str__(self):
        return self.stud_name