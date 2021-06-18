from django.urls import path, include   
from . import views

app_name="accounts"

urlpatterns = [
    # 로그인
    path('user/', include('rest_auth.urls')),
    # 회원가입
    path('signup/', include('rest_auth.registration.urls')),
    # 회원가입(카카오)
    path('checked/', views.checked, name='checked'),
    # 유저정보추가(최초 로그인시)
    path('initinfo/<int:user_pk>/', views.initinfo, name='initinfo'),
    # 유저정보불러오기
    path('userinfo/<int:user_pk>/', views.userinfo, name='userinfo'),
    # 유저정보수정
    path('updated/', views.updated, name='updated'),
    # 바디 정보 다주기
    path('everybody/', views.everybody, name='everybody'),
    # 바디 측정
    path('bodyupload/', views.bodyupload, name='bodyupload'),
    # 바디 비교
    path('bodylist/', views.bodylist, name='bodylist'),
    # 바디 유무
    path('checkbody/', views.checkbody, name='checkbody/'),
    # """
    # # Diary 생성
    # path('create', views.create, name='create')
    # # Diary 수정
    # path('update', views.update, name='update')
    # # Diary 삭제
    # path('delete', views.delete, name='delete')
    # """
    # path('diary/', views.DiaryAPIView.as_view()),
    # path('diary/<int:pk>/',views.DiaryDetailAPIView.as_view()),
]
