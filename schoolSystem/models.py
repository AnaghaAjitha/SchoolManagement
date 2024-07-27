from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    #role_type=(('teacher','Teacher'),('student','Student'))
    #role = models.CharField(choices=role_type,max_length=20,blank=True,null=True,default=None)
    user_id_choices=[
        ('S','Student'),
        ('T','Teacher'),
        ('N','Non-Teaching Staff'),]
    user_type=models.CharField(max_length=1,choices=user_id_choices,blank=True)

class Course(models.Model):
    course_id=models.CharField(max_length=20,primary_key=True)
    course_name=models.CharField(max_length=30)
    
class Class(models.Model):
    class_id=models.CharField(max_length=10,primary_key=True)
    class_name=models.CharField(max_length=100)
    course=models.ForeignKey(Course,on_delete=models.CASCADE,null=True,blank=True)
    
class Subject(models.Model):
    subject_id=models.CharField(max_length=100,blank=True,null=True)
    name=models.CharField(max_length=100)
    course=models.ForeignKey(Course,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return self.name

class Student(models.Model):
    student_id=models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True,limit_choices_to={'user_type': 'S'})
    date_of_birth= models.DateField()
    address=models.CharField(max_length=225)
    gender=models.CharField(max_length=10)
    phone_no=models.CharField(max_length=20,null=True,blank=True)
    class_room=models.ForeignKey(Class,on_delete=models.CASCADE,null=True,blank=True)
    
class Staff(models.Model):
    staff_id=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,limit_choices_to={'user_type__in':['T','N']})
    joining_date=models.DateField()
    phone_no=models.CharField(max_length=20)
    salary=models.DecimalField(max_digits=10, decimal_places=2)
    
class StudentAttendence(models.Model):
    student_id=models.ForeignKey(Student, on_delete=models.CASCADE)
    class_room=models.ForeignKey(Class, on_delete=models.CASCADE)
    working_day=models.CharField(max_length=10)
    status=models.CharField(max_length=10)
    
class StaffAttendence(models.Model):
    staff_id=models.ForeignKey(Staff, on_delete=models.CASCADE)
    working_day=models.CharField(max_length=10)
    status=models.CharField(max_length=10)
    
class Room(models.Model):
    room_id=models.AutoField(primary_key=True)
    room_name=models.CharField(max_length=20)
    
class Event(models.Model):
    event_id=models.AutoField(primary_key=True)
    event_name=models.CharField(max_length=50)
    event_date=models.DateField()
    student_in_charge=models.ForeignKey(Student,on_delete=models.CASCADE)
    teacher_in_charge=models.ForeignKey(Staff,on_delete=models.CASCADE)
    venue=models.ForeignKey(Room,on_delete=models.CASCADE)
    

class Exam(models.Model):
    exam_id = models.AutoField(primary_key=True)
    exam_name=models.CharField(max_length=100)
    exam_date=models.DateField()
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    duration=models.IntegerField()
    max_marks= models.DecimalField(max_digits=5,decimal_places=2)
    class_room=models.ForeignKey(Class,on_delete=models.CASCADE)

class Mark(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    exam=models.ForeignKey(Exam,on_delete=models.CASCADE,null=True,blank=True)
    marks_obtained = models.DecimalField(max_digits=5,decimal_places=2)
    
class Enrollment(models.Model):
    enrollment_id=models.AutoField(primary_key=True)
    enrollment_date=models.DateField()
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    student=models.ForeignKey(Student,on_delete=models.CASCADE)

class Schedule(models.Model):
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    class_room=models.ForeignKey(Class,on_delete=models.CASCADE)
    period=models.CharField(max_length=50)


