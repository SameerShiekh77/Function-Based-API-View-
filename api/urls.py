
from django.urls import path
from . import views 
urlpatterns = [
    path('student-list/',views.studentApi,name='index'),
    path('student-list/<int:pk>/',views.studentApi,name='student-details'),
]
