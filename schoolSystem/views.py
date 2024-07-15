#from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .models import User,Subject,Mark
from .serializers import UserSerializer,SubjectSerializer,MarkSerializer

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
    
    
