from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Diet, Body

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        

class BodySerializer(serializers.ModelSerializer):
    class Meta:
        model = Body
        fields = '__all__'

class DietSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diet
        fields = '__all__'

