from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('students/', views.StudentList.as_view()),
    path('students/<int:pk>/', views.StudentDetail.as_view()),

    path('courses/', views.CourseList.as_view()),
    path('courses/<int:pk>/', views.CourseDetail.as_view()),

    path('colleges/', views.CollegeList.as_view()),
    path('colleges/<int:pk>/', views.CollegeDetail.as_view()),
    path('departments/', views.DepartmentList.as_view()),
    path('departments/<int:pk>/', views.DepartmentDetail.as_view()),
    path('majors/', views.MajorList.as_view()),
    path('majors/<int:pk>/', views.MajorDetail.as_view()),
]

urlpatterns += format_suffix_patterns(urlpatterns)
