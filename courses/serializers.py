from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Accredited_Program

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Accredited_Program
        fields = ['title', 'certificate_type', 'mode_of_delivery', 'price', 'duration', 'start_date']


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']