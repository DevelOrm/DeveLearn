from django.urls import path, re_path, include
from user.views import UserInfoView, Duplication_Check, NaverLoginView, NaverLoginCallbackView, NaverLoginCompleteView, ConfirmEmailView, PasswordResetPageView
from dj_rest_auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordResetView)
from dj_rest_auth.registration.views import SocialAccountDisconnectView, VerifyEmailView
from dj_rest_auth.registration.views import VerifyEmailView
from dj_rest_auth.app_settings import api_settings

urlpatterns = [
    path('login/', LoginView.as_view(), name='rest_login'),
    path('logout/', LogoutView.as_view(), name='rest_logout'),
    path('info/', UserInfoView.as_view(), name='user_info'),
    path('duplication/', Duplication_Check.as_view(), name='duplication_check'),
    path('password/change/', PasswordChangeView.as_view(), name='rest_password_change'),
    path('password/reset/', PasswordResetView.as_view(), name='rest_password_reset'),
    path('rest-auth/password/reset/confirm/<str:uidb64>/<str:token>', PasswordResetPageView.as_view(),name='password_reset_confirm'),
    path('registration/', include('dj_rest_auth.registration.urls')),
    re_path(r'^account-confirm-email/$', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', ConfirmEmailView.as_view(), name='account_confirm_email'),
    path('social/disconnect/', SocialAccountDisconnectView.as_view(), name='social_disconnect'),
    path('social/naver/', NaverLoginView.as_view(), name='naver_login'),
    path('social/naver/callback/', NaverLoginCallbackView.as_view(), name='naver_login_callback'),
    path('social/naver/complete/', NaverLoginCompleteView.as_view(), name='naver_login_complete'),
    # path('social/kakao/', KakaoLoginView.as_view(), name='kakao_login'),
    # path('social/kakao/callback/', KakaoLoginCallbackView.as_view(), name='kakao_login_callback'),
    # path('social/kakao/complete/', KakaoLoginCompleteView.as_view(), name='kakao_login_complete'),
]

if api_settings.USE_JWT:
    from rest_framework_simplejwt.views import TokenVerifyView

    from dj_rest_auth.jwt_auth import get_refresh_view

    urlpatterns += [
        path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
        path('token/refresh/', get_refresh_view().as_view(), name='token_refresh'),
    ]
