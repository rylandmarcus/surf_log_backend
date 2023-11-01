from .models import Surfsession
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class SurfsessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Surfsession
        fields = ['id', 'board', 'notes', 'spot', 'size']