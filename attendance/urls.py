from django.urls import path
from .views import *

urlpatterns = [
   path('', login ,name="custom_login"),
   path('groups', group_list, name="grouplist"),
   path('groups/<int:group_id>', student_list, name="studentlist")
]