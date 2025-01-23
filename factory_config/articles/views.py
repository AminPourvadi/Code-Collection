from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Article
from .serializers import ArticleSerializer

class ArticleDetailView(APIView):
    def get(self, request, pk):
        try:
            article = Article.objects.get(pk=pk)
            serializer = ArticleSerializer(article)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Article.DoesNotExist:
            return Response({'error': 'مقاله پیدا نشد'}, status=status.HTTP_404_NOT_FOUND)
