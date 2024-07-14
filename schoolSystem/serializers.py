from rest_framework import serializers
from .models import User,Subject,Mark

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email','first_name','last_name','password','role']
        def create(self,validated_data):
            password=validated_data.pop('password')
            user=User.objects.create(**validated_data)
            user.set_password(password)
            user.save()
            return user

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
        
        
        
