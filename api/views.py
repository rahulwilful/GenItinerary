from django.shortcuts import render
from rest_framework import viewsets
from api.models import User, Department
from api.serializers import UserSerializer, DepartmentSerializer
from rest_framework.decorators import action
from django.http import HttpResponse
from rest_framework.response import Response

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    # department/{department id}/users
    @action(detail=True, methods=['get'])
    def users(self, request, pk=None):
        department = Department.objects.get(pk=pk)
        users = User.objects.filter(department=department)
        user_serializer = UserSerializer(users, many=True, context={'request':request})
        return Response(user_serializer.data)

