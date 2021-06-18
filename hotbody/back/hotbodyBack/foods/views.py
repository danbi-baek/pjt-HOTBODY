from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.contrib.auth import get_user_model
# from django.db.models import Q

from django.core.files.base import ContentFile
from io import BytesIO, StringIO
from django.core.files.uploadedfile import InMemoryUploadedFile
# from django.core.files import temp as tempfile
# from django.core.files.base import File
# __all__ = ('UploadedFile', 'TemporaryUploadedFile', 'InMemoryUploadedFile', 'SimpleUploadedFile')

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import HttpResponse, JsonResponse, Http404

from .models import Food, CustomFood, Diary, Eat
from accounts.models import Body
from .serializers import FoodSerializer, CustomFoodSerializer, DiarySerializer, EatSerializer
from accounts.serializers import BodySerializer
import os, sys, json
from pathlib import Path
from PIL import Image
import torch
import torch.backends.cudnn as cudnn
from models.experimental import attempt_load
from utils.datasets import LoadStreams, LoadImages
from utils.general import (
    check_img_size, non_max_suppression, apply_classifier, scale_coords,
    xyxy2xywh, plot_one_box, strip_optimizer, set_logging)
from utils.torch_utils import select_device, load_classifier, time_synchronized

User = get_user_model()

@api_view(['GET'])
def month(request):
    # print(request.GET)
    pk = request.GET.get('pk')
    month = request.GET.get('month')
    # print(pk, month)
    memo = Diary.objects.all().filter(userNo=pk, diaryDate__startswith=month).order_by('diaryDate')
    ate_food = Eat.objects.all().filter(userNo=pk, date__startswith=month).order_by('date')
    body = Body.objects.all().filter(userNo=pk).exclude(bodyImg__isnull=True).exclude(bodyImg__exact='').order_by('bodyDate')
    memo_data = DiarySerializer(memo, many=True)
    ate_food_data = EatSerializer(ate_food, many=True)
    body_data = BodySerializer(body, many=True)
    return Response({'all_memo_data': memo_data.data, 'all_food_data':ate_food_data.data, 'all_body_data': body_data.data})

@api_view(['GET'])
def date(request):
    # fname = []
    # print(request.data)
    # print(request.GET)
    # day = request.data['date']
    # pk = request.data['pk']
    m = l = d = c = 0
    day = request.GET.get('date')
    pk = request.GET.get('pk')
    # print(day, pk)
    user = get_object_or_404(User, pk=pk)
    # print(user)
    memo = Diary.objects.filter(userNo=pk, diaryDate=day)
    # print(memo)
    img = Eat.objects.all().filter(userNo=pk, date=day)
    # print(img)
    for e in img:
        # print(e.whenEat)
        if e.whenEat == 0:
            ate_food = CustomFood.objects.filter(userNo=pk, eatNo=e.pk)
            if ate_food != '':
                for k in ate_food:
                    # print(k.kcal)
                    m += k.kcal
        elif e.whenEat == 1:
            ate_food = CustomFood.objects.filter(userNo=pk, eatNo=e.pk)
            if ate_food != '':
                for k in ate_food:
                    l += k.kcal
        elif e.whenEat == 2:
            ate_food = CustomFood.objects.filter(userNo=pk, eatNo=e.pk)
            if ate_food != '':
                for k in ate_food:
                    d += k.kcal
        else:
            ate_food = CustomFood.objects.filter(userNo=pk, eatNo=e.pk)
            if ate_food != '':
                for k in ate_food:
                    c += k.kcal
            
    # print(m, l, d, c)
    # for i in ate_food:
    #     print(i.kcal)
    # print(ate_food)
    # food_kcal = Food.objects.all()
    memo_data = DiarySerializer(memo, many=True)
    # print(memo_data)
    # if ate_food != '':
    #     ate_food_data = CustomFoodSerializer(ate_food, many=True)
    # print(ate_food_data.data)
    img_data = EatSerializer(img, many=True)
    return Response({'memo': memo_data.data, 'EatImg': img_data.data, 'morning': m, 'lunch': l, 'dinner': d, 'snack': c})

@api_view(['POST'])
def upload(request):
    # pass
    # flag = 0
    # def resizing(imgf, flag):
    #     img = Image.open(imgf)
    #     # print(img.size[0])
    #     nw = img.size[0]
    #     nh = img.size[1]
    #     temp = 1
    #     tt = 0
    #     if nw > 1500:
    #         # temp = nw // 416
    #         tt = 1
    #     elif nh > 1500:
    #         # temp = nh // 416
    #         tt = 2

    #     if tt == 1:
    #         nw = nw // 2
    #     elif tt == 2:
    #         nw = nh // 2
    #         # flag = nw
    #         # print('nw:' + nw)
    #     # if(nh > 480):
    #     #     yh = int(nh/480)
    #     #     nh = int(nh/yh)
    #     #     # print('nh:' + nh)
    #     #     flag = 2
    #     # # img.size()

    #     img = img.resize((nw, nw))

    #     # print(nw)

    #     # if flag != 0:
    #     flag = nw
    #     # img.save(img.filename, quality=60)
    #     # print(type(img))
    #     # print(imgf.filename)
    #     # print(img.filename)
    #     # img_resize.save('./test2.jpg')
    #     # def cropper(original_image, crop_coords):
    #     img_io = BytesIO()
    #     # original_image = Image.open(original_image)
    #     # cropped_img = original_image.crop((0, 0, 165, 165))
    #     img.save(img_io, format="PNG")
    #     thumb = InMemoryUploadedFile(img_io, None, str(imgf), 'image/jpeg',img_io, None)
    #     return thumb, flag
    #     # return img
    #     # InMemoryUploadedFile(img_resize, 'ImageField', imgf, 'image/jpeg', sys.getsizeof(img_resize), None)
    #     # 함수로말고 그냥 파일들어오는거 리사이징하고
    #     # 경로적고 해보자

    # print(type(request.FILES['file']))
    # print(request.FILES['file'])
    uimg = request.FILES['file']
    # print(request.POST)
    # b = a.readlines()
    # bbb = Image.open(uimg)
    # print(b)
    # for c in a:
    #     print(c)
    # if bbb.size[0] > 1500:
    #     uimg, flag = resizing(request.FILES['file'], 0)
    # print(type(uimg))
    # InMemoryUploadedFile(uimg)
    # print(type(uimg))
    # print(uimg)
    pk = request.POST['pk']
    user = get_object_or_404(User, pk=pk)
    # print(uimg)
    # print(User)
    # print(request.POST)
    # print(user + '-------foodupload--------')
    eat = Eat.objects.create(
        userNo = user,
        whenEat = request.POST['type'],
        date = request.POST['date'],
        eatImg = uimg
    )
    # print(1)
    eat.save()
    # print(2)
    foods = Eat.objects.order_by('-pk').filter(userNo=pk)[0]
    # print(foods.eatImg)
    img_path = './media/' + str(foods.eatImg)

    aaa = Image.open(uimg)

    source, weights, imgsz = img_path, './models/best100.pt', 480

    # print(imgsz)
    # print(aaa.size[0])
    # Initialize
    set_logging()
    device = select_device('')

    half = device.type != 'cpu'  # half precision only supported on CUDA

    # Load model
    model = attempt_load(weights, map_location=device)  # load FP32 model
    imgsz = check_img_size(imgsz, s=model.stride.max())  # check img_size
    if half:
        model.half()  # to FP16

    # Second-stage classifier
    classify = False

    names = model.module.names if hasattr(model, 'module') else model.names

    save_img = True
    dataset = LoadImages(source, img_size=imgsz)

    img = torch.zeros((1, 3, imgsz, imgsz), device=device)  # init img
    # run once
    _ = model(img.half() if half else img) if device.type != 'cpu' else None

    for path, img, im0s, vid_cap in dataset:
        img = torch.from_numpy(img).to(device)
        img = img.half() if half else img.float()  # uint8 to fp16/32
        img /= 255.0  # 0 - 255 to 0.0 - 1.0
        if img.ndimension() == 3:
            img = img.unsqueeze(0)

        pred = model(img)[0]

        pred = non_max_suppression(
            pred, 0.5, 0.5)

        if classify:
            pred = apply_classifier(pred, modelc, img, im0s)

        # Process detections
        for i, det in enumerate(pred):  # detections per image

            p, s, im0, temp = path, set(), im0s, []

            gn = torch.tensor(im0.shape)[[1, 0, 1, 0]]
            if det is not None and len(det):
                det[:, :4] = scale_coords(
                    img.shape[2:], det[:, :4], im0.shape).round()

                # Print results
                for c in det[:, -1].unique():
                    n = (det[:, -1] == c).sum()  # detections per class
                    s.add(int(c) + 1) # add to string
                    print(names[int(c)])
                    temp.append(names[int(c)])
                # for *xyxy, conf, cls in reversed(det):
                #     print(int(cls))
                #     print(int(cls))

                    # print(names[int(cls)])
                    # print(conf)

    s = list(s)
    # print(s)
    # print(temp)
    # if len(temp) == 1:
    #     foods.foodname = temp[0]
    #     foods.save()
    # elif len(temp) >= 2:
    #     for i in range(1, len(temp)):
    #         ee = Eat.objects.create(
    #             whenEat = request.POST['type'],
    #             date = request.POST['date'],
    #             eatImg = uimg,
    #             foodname = temp[i]
    #         )
    #         ee.save()
    
    # from sqlalchemy.orm import sessionmaker
    # engine = create_engine('sqlite:///db.sqlite3', echo = True)

    # Session = sessionmaker(bind = engine)
    # session = Session()
    # for i in s:
    #     c1 = Food.objects.filter(pk=int(i))
    #     session.add(c1)
    # session.commit()
    # res = []
    # for i in s:
    food = Food.objects.filter(pk__in=s)
    foods = FoodSerializer(food, many=True)

    uimg_path = img_path[1:]
        # res.append(foods)
    # print(foods.data)
    # ress = json.dumps(res)
    # print(ress)
    return Response({'data': foods.data, 'img': uimg_path })

    # 여기서 파일받아서 ai후 DB에서 서치해서 보내준다.
    # 서치안되면 이미지 저장해주고 정보준다.

class diary(APIView):
    def get_object(self, pk, date):
        try:
            return Diary.objects.get(userNo=pk, diaryDate=date)
        except Diary.DoesNotExist:
            raise Http404
    
    # Diary 생성
    def post(self, request, format=None):
        # print(request.data)
        # print(request.data['params']['pk'])
        # print(request.data['params']['memo'])
        pk=request.data['params']['pk']
        memo = request.data['params']['memo']
        date = request.data['params']['date']
        user = get_object_or_404(User, pk=pk)
        # print(user)
        memo = Diary.objects.create(
            userNo = user,
            memo = memo,
            diaryDate = date
        )
        memo.save()
        # print(memo)
        dmemo = Diary.objects.order_by('-pk').filter(userNo = pk)[0]
        serializer = DiarySerializer(dmemo)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # Diary 조회
    def get(self, request):
        # print(1)
        # print(request.GET)
        pk = request.GET.get('pk')
        date = request.GET.get('date')
        # print(pk, date)
        # print(request.Get)
        dmemo = self.get_object(pk, date)
        serializer = DiarySerializer(dmemo)
        return Response(serializer.data)

    # Diary 수정
    def put(self, request):
        dmemo = self.get_object(request.data['params']['pk'], request.data['params']['date'])
        dmemo.memo = request.data['params']['memo']
        dmemo.save()
        serializer = DiarySerializer(dmemo)
        # print(serializer.data)
        # if serializer.is_valid():
            # serializer.save()
        return Response(serializer.data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        pk = request.GET.get('pk')
        date = request.GET.get('date')
        dmemo = self.get_object(pk, date)
        dmemo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def search(request):
    # print(request.data)
    # print(request.GET)
    # name = request.data['name']
    name = request.GET.get('name')
    foods = Food.objects.filter(name__icontains=name)
    serializer = FoodSerializer(foods, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detail(request):
    # print(request.data)
    # print(request.GET)
    pk = request.GET.get('pk')
    when = request.GET.get('type')
    date = request.GET.get('date')
    name = []

    img = Eat.objects.get(userNo=pk, whenEat=when, date=date)
    # print(img)
    ate = EatSerializer(img)
    # print(ate.data)
    eat = CustomFood.objects.filter(userNo=pk, eatNo=img.pk)
    # print(eat)
    for i in eat:
        name.append(i.name)
    serializer = CustomFoodSerializer(eat, many=True)
    
    foods = Food.objects.filter(name__in=name)
    f = FoodSerializer(foods, many=True)


    return Response({'uploadimg': ate.data,'img':f.data, 'food': serializer.data})

@api_view(['POST'])
def add(request):
    # print(request.POST)
    # print(request.data)
    pk = request.data['params']['pk']
    lis = request.data['params']['lis']
    whenEat = request.data['params']['type']
    date = request.data['params']['date']
    
    # print('=====')
    # print(lis)
    
    user = get_object_or_404(User, pk=pk)
    # print(user)
    # print(1)
    eat = get_object_or_404(Eat, userNo=pk, date=date, whenEat=whenEat)
    # print(2)
    # print(eat)
    # print(eat.pk)
    for i in lis:
        # print(i)
        # print(i.name)
        # print(i['name'])
        eatfood = CustomFood.objects.create(
            userNo = user,
            eatNo = eat,
            name = i['name'],
            kcal = i['kcal'],
            car = i['car'],
            pro = i['pro'],
            fat = i['fat'],
            tsg = i['tsg'],
            gram = i['gram']
        )
        eatfood.save()

    res = CustomFood.objects.all().filter(userNo=pk, eatNo=eat.pk)
    serializer = CustomFoodSerializer(res, many=True)

    return Response(serializer.data)

@api_view(['DELETE'])
def delete(request):
    # print(request.data['pk'])
    # print(request.GET)
    pk = request.GET.get('pk')
    whenEat = request.GET.get('type')
    # name = request.data['name']
    date = request.GET.get('date')

    eat = get_object_or_404(Eat, userNo=pk, date=date, whenEat=whenEat)
    cusfood = CustomFood.objects.filter(userNo=pk, eatNo=eat.pk)
    cusfood.delete()
    # eat.delete()

    # res = CustomFood.objects.all().filter(userNo=pk, eatNo=eat.pk)
    # print(res)
    # serializer = CustomFoodSerializer(res, many=True)
    # print(serializer.data)
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
def delete2(request):
    # print(request.data['pk'])
    # print(request.GET)
    pk = request.GET.get('pk')
    whenEat = request.GET.get('type')
    # name = request.data['name']
    date = request.GET.get('date')

    eat = get_object_or_404(Eat, userNo=pk, date=date, whenEat=whenEat)
    cusfood = CustomFood.objects.filter(userNo=pk, eatNo=eat.pk)
    cusfood.delete()
    eat.delete()

    # res = CustomFood.objects.all().filter(userNo=pk, eatNo=eat.pk)
    # print(res)
    # serializer = CustomFoodSerializer(res, many=True)
    # print(serializer.data)
    return Response(status=status.HTTP_204_NO_CONTENT)