from django.urls import path, include
from rest_framework import routers
from user.views import UserViewSet, KakaoLogin, NaverLogin, GoogleLogin

router = routers.DefaultRouter()
router.register('info', UserViewSet)

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('', include(router.urls)),
    path('registration/', include('dj_rest_auth.registration.urls')),
    path('social/kakao/', KakaoLogin.as_view(), name='kakao_login'),
    path('social/naver/', NaverLogin.as_view(), name='naver_login'),
    path('social/google/', GoogleLogin.as_view(), name='google_login'),
    ]