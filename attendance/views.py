from django.shortcuts import render, redirect
from school.models import StudentGroup, Student, Teacher
from .models import *
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
# Create your views here.

def login(request):
	if request.method=='GET':
		return render(request, 'login.html')

	if request.method=='POST':
		data = request.POST
		user = authenticate(request, username=data.get('username'), password = data.get('password'))
		if user is not None:
			dj_login(request, user)
			return redirect('grouplist')
		else:
			return render(request, 'login.html')


def group_list(request):
	if(request.user is None):
		return redirect('login.html')
	teacher = Teacher.objects.all().filter(user_id=request.user.id)
	if(len(list(teacher))):
		teacher = list(teacher)[0]
	else:
		return redirect('custom_login')

	groups = teacher.StudentGroup.all()
	context={
		'groups':groups
	}
	return render(request, 'group_list.html', context)

def student_list(request, group_id):
	if(request.user is None):
		return redirect('login.html')
	if request.method=='GET':
		students = Student.objects.filter(group=group_id)
		context = {
			'students':students
		}
		return render(request, 'student_list.html', context)
	if request.method=='POST':
		data=dict(request.POST)
		group=list(StudentGroup.objects.all().filter(id=group_id))[0]
		del data['csrfmiddlewaretoken']
		for k,v in data.items():
			if len(list(Attendance.objects.all().filter(student_id=list(Student.objects.all().filter(id=k))[0],
					group_id=group,
					date=timezone.now()
				)))!=0:
				attendance=list(Attendance.objects.all().filter(student_id=list(Student.objects.all().filter(id=k))[0],
					group_id=group,
					date=timezone.now()
				))[0]
			else:
				attendance=Attendance()
			attendance.student_id=list(Student.objects.all().filter(id=k))[0]
			attendance.status=v[0]
			attendance.group_id=group
			attendance.save()
		return redirect('grouplist')