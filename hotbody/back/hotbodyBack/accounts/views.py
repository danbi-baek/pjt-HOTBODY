from django.shortcuts import render, redirect, get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse, Http404
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

from .models import User, Body, Diet
from foods.models import Food, Eat, CustomFood
from .serializers import UserSerializer, BodySerializer, DietSerializer
from foods.serializers import FoodSerializer, EatSerializer, CustomFoodSerializer

import sqlite3, datetime

# AI model
from keras.models import load_model
from keras.preprocessing import image
import tensorflow as tf
from tensorflow import Graph, Session

import json, pandas

@api_view(['GET'])
def userinfo(request, user_pk):
    # print(request)
    # print(request.user)
    user = get_object_or_404(User, pk=user_pk)
    serializer = UserSerializer(user)

    body = Body.objects.order_by('-pk').filter(userNo=user_pk)[0]
    body_serializer = BodySerializer(body)
    return Response({'user' : serializer.data, 'body' : body_serializer.data})

@api_view(['PUT'])
def updated(request):
    print(request.data)
    pk = request.data['params']['pk']
    user = get_object_or_404(User, pk=pk)
    body = Body.objects.order_by('-pk').filter(userNo=pk)[0]
    body.height = request.data['params']['height']
    body.weight = request.data['params']['weight']
    body.save()

    user.activity = request.data['params']['activity']
    user.goal = request.data['params']['goal']
    user.nickname = request.data['params']['nickname']
    user.save()

    user = get_object_or_404(User, pk=pk)
    body = Body.objects.order_by('-pk').filter(userNo=pk)[0]

    serializer = UserSerializer(user)
    body_serializer = BodySerializer(body)

    return Response({'user' : serializer.data, 'body' : body_serializer.data})



@csrf_exempt
def checked(request):
    uName = request.body.decode('utf-8')
    name = json.loads(uName)
    checkName = name['username']
    user = User.objects.filter(username=checkName)
    if user:
        data = UserSerializer(user[0])
        return HttpResponse(data, status=200)

    else:
        return HttpResponse(status=400)

@csrf_exempt
def initinfo(request, user_pk):

    request = json.loads(request.body)

    gender = request['gender']
    nickname = request['nickname']
    activity = request['activity']
    goal = request['goal']
    age = int(request['age'])
    height = float(request['height'])
    weight = float(request['weight'])
    bmi = round((weight / (height * height)) * 10000, 2)

    if gender == 1:
        bmr = 655.1 + (9.56 * weight) + (1.85 * height) - (4.68 * age)
    else:
        bmr = 66.47 + (13.75 * weight) + (5 * height) - (6.76 * age)
    dayKcal = (height - 100) * 0.9 * 30

    user = get_object_or_404(User, pk=user_pk)
    user.nickname = nickname
    user.gender = gender
    user.activity = activity
    user.goal = goal
    user.age = age
    user.init = 1
    user.save()

    body = Body.objects.create(
        userNo = user,
        height = height,
        weight = weight,
        # 체질량 지수
        bmi = bmi,
        # 기초대사량
        bmr = bmr,
        # 체지방률 (눈바디)
        fat = 0,
        # 근육량
        muscle = 0,
        # 하루권장칼로리
        dayKcal = dayKcal,
    )
    body.save()

    rBody = Body.objects.get(userNo=user_pk)
    serializer = BodySerializer(rBody)
    # print(serializer.data)
    return JsonResponse(serializer.data)

@api_view(['GET'])
def everybody(request):
    kcal = car = fat = pro = 0
    lis = []
    pk = request.GET.get('pk')
    date = request.GET.get('date')
    # print(pk)
    body = Body.objects.order_by('-pk').filter(userNo=pk)
    serializer = BodySerializer(body, many=True)

    eat = Eat.objects.all().filter(userNo=pk, date=date)
    for i in eat:
        lis.append(i.pk)
    ate_food = CustomFood.objects.filter(userNo=pk, eatNo__in=lis)
    for i in ate_food:
        # print(i.kcal)
        kcal += i.kcal
        car += i.car
        fat += i.fat
        pro += i.pro
    
    print(kcal, car, fat, pro)
    # foods = CustomFood.objects.all().filter(userNo=pk, date=date)
    # food_serializer = EatSerializer(foods, many=True)
    return Response({'body': serializer.data, 'kcal': kcal, 'car': car, 'fat': fat, 'pro': pro})

@api_view(['POST'])
@csrf_exempt
def bodyupload(request):
    uploadimg = request.FILES['file']
    pk = request.POST['pk']
    user = get_object_or_404(User, pk=pk)
    # print(user + '------------bodyupload------------')


    img_height, img_width=224,224
    with open('./models/body.json','r',encoding='UTF-8') as f:
        labelInfo=f.read()

    labelInfo=json.loads(labelInfo)


    model_graph = Graph()
    with model_graph.as_default():
        tf_session = Session()
        # print('---read module---')
        with tf_session.as_default():
            if user.gender == 2:
                model=load_model('./models/mannn.h5')
            else:
                model=load_model('./models/woman.h5')



    height = float(request.POST['height'])
    weight = float(request.POST['weight'])
    bmi = round((weight / (height * height)) * 10000, 2)
    age = user.age

    if user.gender == 1:
        bmr = 655.1 + (9.56 * weight) + (1.85 * height) - (4.68 * age)
    else:
        bmr = 66.47 + (13.75 * weight) + (5 * height) - (6.76 * age)
    dayKcal = (height - 100) * 0.9 * 30

    body = Body.objects.create(
        userNo = user,
        bodyImg = uploadimg,
        height = height,
        weight = weight,
        # 체질량 지수
        bmi = bmi,
        # 기초대사량
        bmr = bmr,
        # 체지방률 (눈바디)
        fat = 0,
        # 근육량
        muscle = 0,
        # 하루권장칼로리
        dayKcal = dayKcal,
    )
    body.save()

    
    now = datetime.datetime.now()
    now_Date = now.strftime('%Y-%m-%d')
    # print(type(now_Date))

    result = Body.objects.order_by('-pk').filter(userNo=pk)[0]
    # print(result.bodyImg)
    predictImg = 'media/' + str(result.bodyImg)
    # print(predictImg)

    img = image.load_img(predictImg, target_size=(64, 64))
    x = image.img_to_array(img)
    x=x.reshape(1,64, 64,3)
    x=x/256

    with model_graph.as_default():
        with tf_session.as_default():
            predi=model.predict(x)

    import numpy as np
    predictedLabel=labelInfo[str(np.argmax(predi[0]))]
    print('--예측--')
    print(predi[0][0])
    print(predi[0][1])
    print(predi[0][2])
    print('인덱스: '+str(np.argmax(predi[0])))
    print('라벨 '+predictedLabel)

    temp = np.argsort(-predi,axis=1)
    print(temp)
    
    mainlabel = predi[0][temp[0][0]]
    sublabel = predi[0][temp[0][1]]
    print(f'{mainlabel*100} @@@@@@@@@@ {sublabel*100}')


    # 7.5 // 20 // 30

    # 15 // 25 // 35

    def findFat(fat):
        avgfat = 0
        if fat == 0:
            avgfat = 7.5
        elif fat ==1:
            avgfat = 20
        elif fat == 2:
            avgfat = 30
        return avgfat

    def findFat2(fat):
        avgfat = 0
        if fat == 0:
            avgfat = 15
        elif fat ==1:
            avgfat = 25
        elif fat == 2:
            avgfat = 35
        return avgfat


    if user.gender == 1:
        mainfat = findFat2((temp[0][0]))
        subfat = findFat2((temp[0][1]))
    else:
        mainfat = findFat((temp[0][0]))
        subfat = findFat((temp[0][1]))
    print(f'{mainfat} ======== {subfat}')

    if(temp[0][0] < temp[0][1]) :
        mainfat += (subfat-mainfat) * sublabel
    else:
        mainfat -= (mainfat-subfat) * sublabel

    # print('----')
    # print(mainfat)

    # 여기서
    result.fat = round(mainfat, 2)
    result.muscle = (result.weight - (result.weight * result.fat / 100) - 2.75) * 0.577

    # print(result.muscle * 0.577)
    result.save()
    # sql문 join => serializer 어케쓰지
    # conn = sqlite3.connect("db.sqlite3")
    # cursor = conn.cursor()
    # sql = f"select u.id, u.username, u.age, u.activity, u.gender, u.goal, b.bmi, b.bmr, b.fat, b.muscle, b.dayKcal, b.bodyImg, b.bodyDate from accounts_user u, accounts_body b on u.id = b.userNo_id where u.id = {pk} order by b.id desc LIMIT 1"
    # sql = f"select * from accounts_body b where b.bodyDate = {now_Date}"
    # result2 = cursor.execute(sql)
    # users = cursor.fetchall()
    # print(users)
    u = UserSerializer(user)
    b = BodySerializer(result)


    # serializer = BodySerializer(users)
    # print(serializer.data)

    return Response({'user': u.data, 'body': b.data})

@csrf_exempt
@api_view(['GET'])
def bodylist(request):
    # request = json.loads(request.body)
    print('--------bodylist--------')
    pk = request.GET.get('pk')
    start = request.GET.get('start')
    end = request.GET.get('end')

    # from_to = pandas.date_range(start, end)

    # b_list = []

    # for i in from_to:
        # print(i)
        # b_list.append(BodySerializer(Body.objects.filter(bodyDate=i, userNo=pk)))
    # body = (Body.objects.filter(bodyDate=from_to, userNo=pk))
    # print("여기는 b_list")
    # print(b_list)
    # print(1)
    b_list = Body.objects.filter(bodyDate__range=[start, end], userNo=pk).exclude(bodyImg__isnull=True).exclude(bodyImg__exact='')
    # print(b_list)
    serializer = (BodySerializer(b_list, many=True))
    # print(2)
    # serializer = BodySerializer(b_list[0])
    # print(serializer)
    # print(body)
    return Response(serializer.data)

@api_view(['GET'])
def checkbody(request):
    pk = request.GET.get('pk')
    # print(pk)
    try:
        check = Body.objects.order_by('-pk').filter(userNo=pk).exclude(bodyImg__isnull=True).exclude(bodyImg__exact='')[0]
        # print(check)
        checku = get_object_or_404(User, pk=pk)
        # print(checku)
        c_body = BodySerializer(check)
        # print(c_body)
        c_user = UserSerializer(checku)
        # print(c_user.data)
        return Response({'body': c_body.data, 'user': c_user.data })
    except:
        return HttpResponse(status=400)
