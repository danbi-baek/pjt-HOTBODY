from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    nickname = models.CharField(max_length=100)
    gender = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    activity = models.IntegerField(blank=True, null=True)
    goal = models.IntegerField(blank=True, null=True)
    init = models.IntegerField(default=0)
    # img = models.ImageField(blank=True, null=True)

class Diet(models.Model):
    goal = models.IntegerField(blank=True, null=True)
    recommendImg = models.ImageField(blank=True, null=True)

class Body(models.Model):
    userNo = models.ForeignKey(User, on_delete=models.CASCADE)
    bodyDate = models.DateField(auto_now_add=True)
    bodyImg = models.ImageField(blank=True, null=True, upload_to="body/%Y/%m/%d")
    bmi = models.FloatField()
    bmr = models.FloatField()
    fat = models.FloatField()
    muscle = models.FloatField()
    height = models.FloatField()
    weight = models.FloatField()
    dayKcal = models.FloatField()
