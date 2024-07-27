from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True, required=False)
    class Meta:
        model=User
        fields=['id','username','first_name','last_name','email','user_type','password']
        extra_kwargs={
            'password':{'write_only':True},
            'user_type':{'required':True},
        }
    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists.")
        return value
        
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'
        
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Subject
        fields='__all__'


class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model=Mark
        fields='__all__'
        
class StaffSerializer(serializers.ModelSerializer):
        class Meta:
            model=Staff
            fields='__all__'

class ClassSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Class
        fields='__all__'
        
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields='__all__'

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model=Exam
        fields='__all__'
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model=Room
        fields=['room_id', 'room_name']
        
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event
        fields='__all__'

class StudentAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentAttendence
        fields=['student_id', 'class_id', 'working_day', 'status']

class StaffAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model=StaffAttendence
        fields=['staff_id', 'working_day', 'status']
        
# class GuardianSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Guardian
#         fields=['guardian_id','stud_id','guardian_name','relationship','phone_no']
        
class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Enrollment
        fields='__all__'

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Schedule
        fields='__all__'
