#from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .models import *
from .serializers import *

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset=Subject.objects.all()
    serializer_class=SubjectSerializer
    
class MarkViewSet(viewsets.ModelViewSet):
    queryset=Mark.objects.all()
    serializer_class=MarkSerializer
    
class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    
class StaffViewSet(viewsets.ModelViewSet):
    queryset=Staff.objects.all()
    serializer_class=StaffSerializer
    
class ClassViewSet(viewsets.ModelViewSet):
    queryset=Class.objects.all()
    serializer_class=ClassSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer
    
class ExamViewSet(viewsets.ModelViewSet):
    queryset=Exam.objects.all()
    serializer_class=ExamSerializer
    
class StudentAttendenceViewSet(viewsets.ModelViewSet):
    queryset=StudentAttendence.objects.all()
    serializer_class=StudentAttendanceSerializer
    
class StaffAttendenceViewSet(viewsets.ModelViewSet):
    queryset=StaffAttendence.objects.all()
    serializer_class=StaffAttendanceSerializer
    
class EventViewSet(viewsets.ModelViewSet):
    queryset=Event.objects.all()
    serializer_class=EventSerializer
    
class RoomViewSet(viewsets.ModelViewSet):
    queryset=Room.objects.all()
    serializer_class=RoomSerializer
    
class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset=Enrollment.objects.all()
    serializer_class=EnrollmentSerializer

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset=Schedule.objects.all()
    serializer_class=ScheduleSerializer
