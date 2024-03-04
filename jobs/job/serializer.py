from rest_framework import serializers
from .models import Job,JobApply
from rest_framework import filters


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model =Job
        fields = '__all__'



class JobApplySerializer(serializers.ModelSerializer):
    class Meta:
        model =JobApply
        fields = '__all__'