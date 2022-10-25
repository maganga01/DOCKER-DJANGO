from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from accounts.models import Company, Talent
from accounts.serializers import ProjectSerializer, RoleSerializer, TalentSerializer, CompanySerializer, Project
from .models import Role, Talent, Company, Project
from rest_framework import mixins
from rest_framework import generics

from rest_framework import routers, serializers, viewsets

class TalentViewSet(viewsets.ModelViewSet):
    queryset = Talent.objects.all()
    serializer_class = TalentSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
