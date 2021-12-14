from django.db.models.query import QuerySet
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, viewsets, permissions, response, status
from .serializers import *
from .models import *


class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        queryset = Task.objects.filter(owner=self.request.user).order_by('deadline')
        return queryset

class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    def get_queryset(self):
        if self.request.user.is_staff:
            queryset = Categori.objects.all()
        else:
            queryset = Categori.objects.filter(owner=self.request.user)
        return queryset

    def destroy(self, request, *args, **kwargs):
        if request.user.is_staff:
            obj = self.get_object()
            self.perform_destroy(obj)
            return response.Response(status=status.HTTP_204_NO_CONTENT)
        return response.Response(status=status.HTTP_400_BAD_REQUEST, data="You are not allowed to delete!")

    




