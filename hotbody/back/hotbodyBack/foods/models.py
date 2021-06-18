from django.db import models
from django.conf import settings
# from uuid import uuid4
# from django.utils import timezone



# photo = models.ImageField(upload_to=date_upload_to)

class Food(models.Model):
    name = models.CharField(max_length=100)
    kcal = models.IntegerField(blank=True, null=True)
    car = models.IntegerField(blank=True, null=True)
    pro = models.IntegerField(blank=True, null=True)
    fat = models.IntegerField(blank=True, null=True)
    tsg = models.IntegerField(blank=True, null=True)
    foodImg = models.ImageField(blank=True, null=True)
    gram = models.IntegerField(default=100)

class Diary(models.Model):
    userNo = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    memo = models.TextField()
    diaryDate = models.CharField(max_length=100)
    
class Eat(models.Model):
    userNo = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 아침, 점심, 저녁 중 언제 먹었는지
    whenEat = models.IntegerField(blank=True, null=True)
    # foodname = models.CharField(max_length=100, blank=True, null=True)
    eatImg = models.ImageField(blank=True, null=True, upload_to="eat/%Y/%m/%d")
    # 날짜
    date = models.CharField(max_length=100)

class CustomFood(models.Model):
    """ 파일명 지정
    def date_upload_to(instance, filename):
        # upload_to="%Y/%m/%d" 처럼 날짜로 세분화
        ymd_path = timezone.now().strftime('%Y/%m/%d') 
        # 길이 32 인 uuid 값
        uuid_name = uuid4().hex
        # 확장자 추출
        extension = os.path.splitext(filename)[-1].lower()
        # 결합 후 return
        return '/'.join([
            ymd_path,
            uuid_name + extension,
        ])
    """
    userNo = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    eatNo = models.ForeignKey(Eat, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    kcal = models.IntegerField(blank=True, null=True)
    car = models.IntegerField(blank=True, null=True)
    pro = models.IntegerField(blank=True, null=True)
    fat = models.IntegerField(blank=True, null=True)
    tsg = models.IntegerField(blank=True, null=True)
    gram = models.IntegerField(default=100)
    # foodImg = models.ImageField(blank=True, null=True, upload_to="custom/%Y/%m/%d")
    # amount = models.FloatField()
