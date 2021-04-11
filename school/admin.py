from django.contrib import admin
from django import forms
from .models import *
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


class AttendanceForm(forms.ModelForm):
	student_name = forms.CharField()
	status = (
        ('P', 'Present'),
        ('A', 'Absent'),
        ('L', 'Late'),
    )
	status = forms.ChoiceField(choices = status)

	def __init__(self, *args, **kwargs):
		super(AttendanceForm, self).__init__(*args, **kwargs)
		self.fields['student_name'].queryset = Student.objects.get(
			group=self.instance.pk).firstname

	class Meta:
		fields = ('name','student_name', 'status')


	
@admin.register(StudentGroup)
class StudentGroupAdmin(admin.ModelAdmin):
	form =AttendanceForm



@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
	pass






