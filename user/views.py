from allauth.socialaccount.providers.kakao.views import KakaoOAuth2Adapter
from allauth.socialaccount.providers.naver.views import NaverOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView

from rest_framework import viewsets
from rest_framework import serializers
from user.models import User

from drf_spectacular.utils import OpenApiExample, OpenApiParameter, extend_schema_view, extend_schema, OpenApiTypes
from rest_framework.decorators import action


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'nickname', 'last_login', 'joined_date', 'is_teacher']


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class KakaoLogin(SocialLoginView):
    adapter_class = KakaoOAuth2Adapter

class NaverLogin(SocialLoginView):
    adapter_class = NaverOAuth2Adapter

class GoogleLogin(SocialLoginView):
    callback_url = 'http://127.0.0.1:8000/user/google/login/callback/'
    client_class = OAuth2Client
    adapter_class = GoogleOAuth2Adapter