from django.shortcuts import render
from .models import Surfsession
from rest_framework import viewsets, permissions
from .serializers import SurfsessionSerializer

# Create your views here.
class SurfsessionViewSet(viewsets.ModelViewSet):
    queryset = Surfsession.objects.all()
    serializer_class = SurfsessionSerializer
    permission_classes = [permissions.AllowAny] #Coule be [permissions.IsAuthenticated]
    