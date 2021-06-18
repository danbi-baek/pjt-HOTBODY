# from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Food, CustomFood, Eat, Diary

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'

class CustomFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomFood
        fields = '__all__'

class EatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eat
        fields = '__all__'

class DiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = '__all__'