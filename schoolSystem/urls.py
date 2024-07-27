from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'users',UserViewSet)
router.register(r'subjects',SubjectViewSet)
router.register(r'marks',MarkViewSet)
router.register(r'student',StudentViewSet)
router.register(r'staff',StaffViewSet)
router.register(r'exam',ExamViewSet)
router.register(r'event',EventViewSet)
router.register(r'room',RoomViewSet)
router.register(r'Student Attendence',StudentAttendenceViewSet)
router.register(r'course',CourseViewSet)
router.register(r'Staff Attendence',StaffAttendenceViewSet)
router.register(r'enrollments', EnrollmentViewSet)
router.register(r'schedules', ScheduleViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('token/', views.obtain_auth_token)


]
