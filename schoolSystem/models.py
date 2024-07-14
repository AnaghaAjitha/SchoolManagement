from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    role_type=(('teacher','Teacher'),('student','Student'))
    role = models.CharField(choices=role_type,max_length=20,blank=True,null=True)

    
class Subject(models.Model):
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Mark(models.Model):
    student = models.ForeignKey(User,on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    marks_obtained = models.DecimalField(max_digits=5,decimal_places=2)
    