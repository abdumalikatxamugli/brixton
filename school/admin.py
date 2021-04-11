from django.contrib import admin
from django import forms
from .models import *
from django.contrib.auth.models import User
# Register your models here.

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
	pass
	


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
	pass



@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
	pass




	
@admin.register(StudentGroup)
class StudentGroupAdmin(admin.ModelAdmin):
	pass



@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
	pass






