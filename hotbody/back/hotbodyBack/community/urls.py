from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    # 게시판 CRUD
    path('board/', views.board.as_view(), name='board'),
    path('detail/<int:boardpk>', views.detail, name='detail'),
]