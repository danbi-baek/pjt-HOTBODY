from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model

from .models import Article
from .serializers import ArticleSerializer

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

User = get_user_model()


class board(APIView):
    # 글 생성
    def post(self, request, format=None):
        # print(request.POST)
        # print(request.data)
        # print(request.data['params']['pk'])
        # print(request.data['params']['memo'])
        # pk=request.data['params']['pk']
        # title = request.data['params']['title']
        # content = request.data['params']['content']
        pk=request.data['pk']
        title = request.data['title']
        content = request.data['content']
        img = request.FILES['file']

        content = content.replace("\n", "<br>")
        user = get_object_or_404(User, pk=pk)
        # print(user)
        article = Article.objects.create(
            userNo = user,
            title = title,
            content = content,
            articleImg = img
        )
        article.save()
        # print(memo)
        article = Article.objects.order_by('-pk').filter(userNo = pk)[0]
        serializer = ArticleSerializer(article)
        # print(serializer.data)
        return Response(serializer.data)

    # 글 조회
    def get(self, request):
        articles = Article.objects.all().order_by('-pk')
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    # 글 수정
    def put(self, request):
        # article = Article.objects.filter(userNo=request.data['params']['pk'], pk=request.data['params']['boardpk'])
        # article.title = request.data['params']['title']
        # article.content = request.data['params']['content']
        article = Article.objects.get(userNo=request.data['pk'], pk=request.data['boardpk'])
        # print(article, article.title, article.content)
        article.title = request.data['title']
        article.content = request.data['content']
        article.save()
        
        serializer = ArticleSerializer(article)
        # print(serializer.data)
        return Response(serializer.data)
    
    def delete(self, request):
        # print(request.GET)
        # print(request.data)
        # pk = request.GET.get('pk')
        # boardpk = request.GET.get('boardpk')
        pk = request.data['pk']
        boardpk = request.data['boardpk']
        article = Article.objects.get(userNo=pk, pk=boardpk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def detail(request, boardpk):
    article = Article.objects.get(pk=boardpk)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)
