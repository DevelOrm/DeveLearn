from django.shortcuts import render
from django.core.paginator import Paginator
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.response import Response
from .models import News
from datetime import datetime
from .serializers import NewsSerializer


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


class NewsListView(generics.ListAPIView):
    queryset = News.objects.all().order_by('-written_at')
    serializer_class = NewsSerializer
    pagination_class = PageNumberPagination


class NewsRecentView(generics.ListAPIView):
    queryset = News.objects.all().order_by('-written_at')[:6]
    serializer_class = NewsSerializer
    pagination_class = PageNumberPagination


class NewsSearchView(generics.ListAPIView):
    serializer_class = NewsSerializer

    def get_queryset(self):
        keyword = self.request.query_params.get('q')  # 브라우저에서 제공한 키워드
        if keyword:
            queryset = News.objects.filter(
                title__icontains=keyword)[:100]  # 제목에 키워드를 포함하는 객체 검색
        else:
            queryset = News.objects.all()[:100]
        paginator = Paginator(queryset, 10)  # 10개씩 페이지 처리
        page = self.request.query_params.get('page', 1)
        results = paginator.get_page(page)
        return results

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        response_data = {
            'results': serializer.data,
            'count': queryset.paginator.count,
            'page_size': queryset.paginator.per_page
        }
        return Response(response_data)
