from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from .models import News


class NewsBotView(APIView):
    def post(self, request):

        data = request.data

        for i in data:
            news = data[i]
            news_exists = News.objects.filter(title=news['title']).exists()
            if news_exists:
                continue

            written_at = datetime.strptime(
                news['time'], "%Y-%m-%d %H:%M:%S.%f")

            # link의 길이가 urlfield(max_length=2048)을 초과하는 경우 예외 처리
            try:
                News.objects.create(
                    title=news['title'],
                    link=news['link'],
                    written_at=written_at,
                )
            except:
                pass

        return Response({'message': 'JSON data received successfully'}, status=status.HTTP_201_CREATED)
