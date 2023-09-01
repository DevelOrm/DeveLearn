from rest_framework import serializers
from .models import News

from drf_spectacular.utils import OpenApiExample, OpenApiParameter, extend_schema_view, extend_schema, OpenApiTypes, \
    extend_schema_serializer
from rest_framework.decorators import action


# @extend_schema_serializer(
#     # summary="크롤링된 뉴스 데이터 추가",
#     description="크롤링된 뉴스 데이터 추가",
#     # tags=["News"],
# )
class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
