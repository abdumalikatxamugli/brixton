from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Subject(models.Model):
	name = models.CharField(max_length = 128)

	def __str__(self):
		return self.name

class Level(models.Model):
	name = models.CharField(max_length = 256)
	def __str__(self):
		return self.name


class StudentGroup(models.Model):
	name = models.CharField(max_length = 128)
	level = models.ForeignKey(Level, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Teacher(User):
	firstname = models.CharField(max_length=256)
	lastname = models.CharField(max_length=256)
	phone = models.CharField(max_length = 14)
	birthdate = models.DateField()
	ielts = models.ImageField(upload_to = 'teachers')
	passport_upload = models.ImageField(upload_to = 'teachers')
	subject =  models.ManyToManyField(Subject)
	StudentGroup = models.ManyToManyField(StudentGroup)
	class Meta:
		verbose_name = "Teacher"




class Student(models.Model):
	firstname = models.CharField(max_length=256)
	lastname = models.CharField(max_length=256)
	phone = models.CharField(max_length = 14)
	group = models.ManyToManyField(StudentGroup)

	def __str__(self):
		return self.firstname


	

class Attendance(models.Model):
	student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
	group_id = models.ForeignKey(StudentGroup, on_delete = models.CASCADE)
	date = models.DateField(default = timezone.now())
	status = (
        ('P', 'Present'),
        ('A', 'Absent'),
        ('L', 'Late'),
    )
	status = models.CharField(max_length=1, choices = status)
