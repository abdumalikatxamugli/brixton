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

class Teacher(models.Model):
	user_id = models.OneToOneField(User, on_delete=models.CASCADE)
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

	def __str__(self):
		return self.firstname+" "+self.lastname



class Student(models.Model):
	firstname = models.CharField(max_length=256)
	lastname = models.CharField(max_length=256)
	phone = models.CharField(max_length = 14)
	group = models.ManyToManyField(StudentGroup)

	def __str__(self):
		return self.firstname


	
