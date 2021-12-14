from django.urls import path
from django.urls.conf import include, include
from rest_framework import routers
from .views import *
from todo.views import TaskView

router = routers.DefaultRouter()
router.register(r'tasks', TaskView, basename='Task')
router.register(r'categories', CategoryView, basename='Category')

urlpatterns = [
    path('', include(router.urls)),   
]
