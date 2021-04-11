from django.db import models
from school.models import *
from django.utils import timezone

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

