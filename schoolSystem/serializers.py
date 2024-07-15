from rest_framework import serializers
from .models import User,Subject,Mark

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ['id','username','first_name','last_name','email','role']

        def validate_username(self,value):
            if User.objects.filter(username=value).exists():
                raise serializers.ValidationError("Username already exists.")
            return value
        

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Subject
        fields=['id','name']
        

class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model=Mark
        fields=['id','student','subject','marks_obtained']
        
        
        
