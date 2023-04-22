from django.urls import path, include
from rest_framework import routers
from .views import CourseViewset, TeacherViewset,LessonViewset

router = routers.DefaultRouter()
router.register(r'course',CourseViewset, basename='course')
router.register(r'teacher',TeacherViewset, basename='teacher')
router.register(r'lesson',LessonViewset, basename='lesson')

urlpatterns = [
    path('',include(router.urls))
]

