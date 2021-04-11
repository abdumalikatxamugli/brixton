from django.contrib import admin
from .models import *
from rangefilter.filters import DateRangeFilter

# Register your models here.

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):

	list_display=('student_id', 'status', 'group_id', 'date')
	list_filter  = ('group_id',('date', DateRangeFilter))
	
	