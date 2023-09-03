#from allauth.socialaccount.providers.kakao.views import KakaoOAuth2Adapter
from allauth.socialaccount.providers.naver.views import NaverOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from dj_rest_auth.views import PasswordResetConfirmView
from allauth.account.models import EmailConfirmation, EmailConfirmationHMAC

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from user.models import User
from user.serializers import UserInfoSerializer, UseridDuplicationCheckSerializer, NicknameDuplicationCheckSerializer, EmailDuplicationCheckSerializer, PhonenumberDuplicationCheckSerializer

import requests
from user.util import nickname_generate

import os
import re
import environ
from pathlib import Path
from django.shortcuts import redirect

from drf_spectacular.utils import extend_schema


BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))


class UserInfoView(APIView):
    @extend_schema(
        summary="유저 정보 조회",
        description="유저 정보 조회",
        tags=["User"],
        responses=UserInfoSerializer,
    )
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

    @extend_schema(
        summary="유저 정보 수정",
        description="유저 정보 수정",
        tags=["User"],
        request=UserInfoSerializer,
        responses=UserInfoSerializer,
    )
    def patch(self, request):
        user = self.request.user
        if user == 'AnonymousUser':
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
        try:
            queryset = User.objects.get(user_id = user.user_id)
            serializer = UserInfoSerializer(queryset, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @extend_schema(
        summary="유저 삭제",
        description="유저 삭제",
        tags=["User"],
        request=UserInfoSerializer,
        responses=UserInfoSerializer,
    )
    def delete(self, request):
        user = self.request.user
        if user == 'AnonymousUser':
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        try:
            queryset = User.objects.filter(user_id = user.user_id)
            queryset.delete()
            return Response({'message' : 'User Deleted'})
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UseridDuplicationCheck(APIView):
    @extend_schema(
        summary="유저 아이디 중복 체크",
        description="유저 아이디 중복 체크",
        tags=["User"],
        request=UseridDuplicationCheckSerializer,
        responses=UseridDuplicationCheckSerializer,
    )
    def post(self, request):
        serializer = UseridDuplicationCheckSerializer(data=request.data)
        if serializer.is_valid():
            return Response({"message": "중복된 항목이 없습니다."})
        return Response(serializer.errors, status=400)

class NicknameDuplicationCheck(APIView):
    @extend_schema(
        summary="유저 닉네임 중복 체크",
        description="유저 닉네임 중복 체크",
        tags=["User"],
        request=NicknameDuplicationCheckSerializer,
        responses=NicknameDuplicationCheckSerializer,
    )
    def post(self, request):
        serializer = NicknameDuplicationCheckSerializer(data=request.data)
        if serializer.is_valid():
            return Response({"message": "중복된 항목이 없습니다."})
        return Response(serializer.errors, status=400)

class EmailDuplicationCheck(APIView):
    @extend_schema(
        summary="유저 이메일 중복 체크",
        description="유저 이메일 중복 체크",
        tags=["User"],
        request=EmailDuplicationCheckSerializer,
        responses=EmailDuplicationCheckSerializer,
    )
    def post(self, request):
        serializer = EmailDuplicationCheckSerializer(data=request.data)
        if serializer.is_valid():
            return Response({"message": "중복된 항목이 없습니다."})
        return Response(serializer.errors, status=400)

class PhonenumberDuplicationCheck(APIView):
    @extend_schema(
        summary="유저 핸드폰 번호 중복 체크",
        description="유저 핸드폰 번호 중복 체크",
        tags=["User"],
        request=PhonenumberDuplicationCheckSerializer,
        responses=PhonenumberDuplicationCheckSerializer,
    )
    def post(self, request):
        serializer = PhonenumberDuplicationCheckSerializer(data=request.data)
        if serializer.is_valid():
            return Response({"message": "중복된 항목이 없습니다."})
        return Response(serializer.errors, status=400)

class NaverLoginView(APIView):
    @extend_schema(
        summary="네이버 소셜 로그인 요청",
        description="네이버 소셜 로그인 요청",
        tags=["User"],
    )
    def get(self, request):
        client_id = env.str('NAVER_CLIENT_ID')
        callback = env.str('MAIN_DOMAIN') + '/user/social/naver/callback/'
        return redirect(f'https://nid.naver.com/oauth2.0/authorize?response_type=code&client_id={client_id}&redirect_uri={callback}')
    
class NaverLoginCallbackView(APIView):
    @extend_schema(
        summary="네이버 소셜 로그인 콜백",
        description="네이버 소셜 로그인 콜백",
        tags=["User"],
    )
    def get(self, request):
        client_id = env.str('NAVER_CLIENT_ID')
        client_secret = env.str('NAVER_SECRET_KEY')
        code = request.GET.get('code')
        state = request.GET.get('state')

        token_request = requests.get(f"https://nid.naver.com/oauth2.0/token?grant_type=authorization_code&client_id={client_id}&client_secret={client_secret}&code={code}&state={state}")
        token_response_json = token_request.json()
        access_token = token_response_json.get('access_token')

        profile_request = requests.get('https://openapi.naver.com/v1/nid/me',  headers={'Authorization': f"Bearer {access_token}"},)

        if profile_request.status_code != 200:
            return Response({'error': '정보를 가져오는데 실패했습니다.'}, status=status.HTTP_400_BAD_REQUEST)

        profile = profile_request.json().get('response')

        if profile['email'] is None:
            return Response({'error': '이메일을 가져오지 못했습니다.'}, status=status.HTTP_400_BAD_REQUEST)

        if profile['nickname'] is None:
            return Response({'error': '닉네임을 가져오지 못했습니다.'}, status=status.HTTP_400_BAD_REQUEST)

        if profile['mobile'] is None:
            return Response({'error': '핸드폰 번호를 가져오지 못했습니다.'}, status=status.HTTP_400_BAD_REQUEST)
        
        data = {'access_token': access_token, 'code': code}
        accept = requests.post(f"{env.str('MAIN_DOMAIN', default='',)}/user/social/naver/complete/", data=data)
        user = User.objects.get(email=profile['email'])
        if (profile['nickname'] == ''):
            random_nickname = nickname_generate()
            user.nickname = random_nickname
        else:
            user.nickname = profile['nickname']
        user.profile_image = profile['profile_image']
        user.phone_number = profile['mobile']
        user.save()
        return Response(accept.json(), status=status.HTTP_200_OK)


@extend_schema(
        summary="네이버 소셜 로그인 성공",
        description="네이버 소셜 로그인 성공",
        tags=["User"],
    )
class NaverLoginCompleteView(SocialLoginView):
    adapter_class = NaverOAuth2Adapter
    client_class = OAuth2Client


# class KakaoLoginView(APIView):
#     def get(self, request):
#         client_id = env.str('KAKAO_CLIENT_ID')
#         callback = env.str('MAIN_DOMAIN') + "/user/social/kakao/callback/"

#         return redirect(f'https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={callback}&response_type=code&scope=account_email')


# class KakaoLoginCallbackView(APIView): 
#     def get(self, request):
#         client_id = env.str('KAKAO_CLIENT_ID')
#         callback = env.str('MAIN_DOMAIN') + "/user/social/kakao/callback/"
#         code = request.GET.get('code')
#         client_secret = env.str('KAKAO_SECRET_KEY')

#         token_request = requests.get(f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={client_id}&redirect_uri={callback}&code={code}&client_secret={client_secret}")
#         token_response_json = token_request.json()
#         access_token = token_response_json.get('access_token')

#         profile_request = requests.get('https://kapi.kakao.com/v2/user/me', headers={'Authorization': f"Bearer {access_token}"})
        
#         if profile_request.status_code != 200:
#             return Response({'error': '정보를 가져오는데 실패했습니다.'}, status=status.HTTP_400_BAD_REQUEST)
        
#         profile_json = profile_request.json()

#         profile = profile_json.get('kakao_account')

#         print(profile)

#         if profile['email'] is None:
#             return Response({"error": "카카오 계정(이메일)을 가져오지 못했습니다."}, status=status.HTTP_400_BAD_REQUEST)
        
#         # if profile['profile']['nickname'] is None:
#         #     return Response({"error": "닉네임을 가져오지 못했습니다."}, status=status.HTTP_400_BAD_REQUEST)

#         data = {'code': code, 'access_token': access_token}
#         accept = requests.post(
#             f"{env.str('MAIN_DOMAIN')}/user/social/kakao/complete/", data=data
#         )
#         accept_json = accept.json()
#         accept_jwt = accept_json.get('token')

#         user = User.objects.get(email=profile['email'])
#         if (profile['profile']['nickname'] == ''):
#             random_nickname = nickname_generate()
#             user.nickname = random_nickname
#         else:
#             user.nickname = profile['profile']['nickname']
#         user.profile_image = profile['profile']['profile_image_url']
#         user.phone_number = profile['mobile']
#         user.save()
#         return Response(accept.json(), status=status.HTTP_200_OK)

# class KakaoLoginCompleteView(SocialLoginView):
#     adapter_class = KakaoOAuth2Adapter
#     client_class = OAuth2Client

class ConfirmEmailView(APIView):
    @extend_schema(
        summary="이메일 인증 확인",
        description="이메일 인증 확인",
        tags=["User"],
    )
    def get(self, *args, **kwargs):
        self.object = confirmation = self.get_object()
        confirmation.confirm(self.request)
        return redirect(f'http://develearn.co.kr/registration-complete.html')

    def get_object(self, queryset=None):
        key = self.kwargs['key']
        email_confirmation = EmailConfirmationHMAC.from_key(key)
        if not email_confirmation:
            if queryset is None:
                queryset = self.get_queryset()
            try:
                email_confirmation = queryset.get(key=key.lower())
            except EmailConfirmation.DoesNotExist:
                return Response("error", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return email_confirmation

    def get_queryset(self):
        qs = EmailConfirmation.objects.all_valid()
        qs = qs.select_related("email_address__user")
        return qs

class PasswordResetPageView(PasswordResetConfirmView):
    def get(self, request, *args, **kwargs):
        requestURL = request.path
        requestData = requestURL.split("/")

        uid = requestData[-2]
        token = requestData[-1]

        passwordChangePage = 'http://develearn.co.kr' + "?uid=" + uid + "?token=" + token + "/"

        return redirect(passwordChangePage)