from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, SubjectViewSet, MarkViewSet

router = DefaultRouter()
router.register(r'users',UserViewSet)
router.register(r'subjects',SubjectViewSet)
router.register(r'marks',MarkViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),

]