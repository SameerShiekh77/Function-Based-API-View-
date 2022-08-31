
from django.urls import path
from . import views 
urlpatterns = [

    # FUNCTION BASE VIEW
    path('student-list/',views.studentApi,name='index'),
    path('student-list/<int:pk>/',views.studentApi,name='student-details'),


# CLASS BASE VIEW
    path('class-student-list/',views.StudentAPI.as_view(),name='student-details'),
    path('class-student-list/<int:pk>/',views.StudentAPI.as_view(),name='student-details'),
]
