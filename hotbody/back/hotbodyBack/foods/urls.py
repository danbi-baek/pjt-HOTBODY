from django.urls import path
from . import views

app_name = 'foods'

urlpatterns = [
    # O달에 있는 정보 다 가져오기
    path('month/', views.month, name='month'),
    # 하루 단위로 가져오기
    path('date/', views.date, name='date'),
    # 음식사진 업로드 (ai를 위한)
    path('upload/', views.upload, name='upload'),
    # 검색 위한 food data 넘기기
    path('search/', views.search, name='search'),
    # 하루 언제, 뭐먹었는지
    path('detail/', views.detail, name='detail'),
    # 먹은 음식 진짜 등록
    path('add/', views.add, name='add'),
    # 음식 삭제
    path('delete/', views.delete, name='delete'),
     # 음식 삭제
    path('delete2/', views.delete2, name='delete2'),
    # diary CRUD
    path('diary/', views.diary.as_view(), name='diary'),
]
