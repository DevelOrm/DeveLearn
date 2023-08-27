from allauth.socialaccount.providers.kakao.views import KakaoOAuth2Adapter
from allauth.socialaccount.providers.naver.views import NaverOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from user.models import User
from user.serializers import UserInfoSerializer

class UserInfoView(APIView):
    def get(self, request):
        user = self.request.user
        if user == 'AnonymousUser':
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
        try:
            queryset = User.objects.filter(user_id = user.user_id)
            serializer = UserInfoSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class KakaoLogin(SocialLoginView):
    adapter_class = KakaoOAuth2Adapter

class NaverLogin(SocialLoginView):
    adapter_class = NaverOAuth2Adapter

class GoogleLogin(SocialLoginView):
    callback_url = 'http://127.0.0.1:8000/user/google/login/callback/'
    client_class = OAuth2Client
    adapter_class = GoogleOAuth2Adapter