from rest_framework import serializers
from dj_rest_auth.serializers import LoginSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.core.exceptions import ValidationError as DjangoValidationError
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from user.models import User
from user.util import nickname_generate

import re


class UserRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(allow_null=True)
    profile_image = serializers.ImageField(allow_null=True)
    phone_number =  serializers.CharField(allow_null=True)
    is_teacher = serializers.BooleanField()

    def validate_phone_number(self, phone_number):
        pattern = r'^01[0-9]{1}-[0-9]{4}-[0-9]{4}$'

        if not re.match(pattern, phone_number):
            raise serializers.ValidationError("올바른 핸드폰 번호를 입력해주세요.")

        if phone_number == None:
            raise serializers.ValidationError("핸드폰 번호를 입력해주세요.")
        if User.objects.filter(phone_number=phone_number).exists():
            raise serializers.ValidationError("이미 사용 중인 핸드폰 번호입니다.")
        return phone_number

    def validate_nickname(self, nickname):
        if User.objects.filter(nickname=nickname).exists():
            raise serializers.ValidationError("이미 사용 중인 닉네임입니다.")
        return nickname

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['nickname'] = self.validated_data.get('nickname', '')
        data['profile_image'] = self.validated_data.get('profile_image', '')
        data['phone_number'] = self.validated_data.get('phone_number', '')
        data['is_teacher'] = self.validated_data.get('is_teacher', '')

        return data
    
    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user = adapter.save_user(request, user, self, commit=False)
        nickname = self.cleaned_data.get("nickname")
        profile_image = self.cleaned_data.get("profile_image")
        phone_number = self.cleaned_data.get("phone_number")
        is_teacher = self.cleaned_data.get("is_teacher")

        if (user.nickname == ""):
            user.nickname = nickname_generate()
        else:
            user.nickname = nickname
        user.profile_image = profile_image
        user.phone_number = phone_number
        user.is_teacher = is_teacher
        if "password1" in self.cleaned_data:
            try:
                adapter.clean_password(self.cleaned_data['password1'], user=user)
            except DjangoValidationError as exc:
                raise serializers.ValidationError(
                    detail=serializers.as_serializer_error(exc)
            )
        user.save()
        self.custom_signup(request, user)
        setup_user_email(request, user, [])
        return user

class UserLoginSerializer(LoginSerializer):
    username = serializers.CharField(required=True, allow_blank=False)
    email = None

class UserInfoSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField()
    email = serializers.ReadOnlyField()
    phone_number = serializers.ReadOnlyField()
    last_login = serializers.ReadOnlyField()
    joined_date = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ['user_id', 'nickname', 'email', 'phone_number', 'profile_image', 'last_login', 'joined_date', 'is_teacher']

class DuplicationCheckSerializer(serializers.Serializer):
    user_id = serializers.CharField(required=True)
    nickname = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    phone_number = serializers.CharField(required=True)

    def validate_user_id(self, input_user_id):
        if User.objects.filter(user_id=input_user_id).exists():
            raise serializers.ValidationError("이미 사용 중인 아이디입니다.")
        return input_user_id
    
    def validate_nickname(self, input_nickname):
        if User.objects.filter(nickname=input_nickname).exists():
            raise serializers.ValidationError("이미 사용 중인 닉네임입니다.")
        return input_nickname
    
    def validate_email(self, input_email):
        if User.objects.filter(email=input_email).exists():
            raise serializers.ValidationError("이미 사용 중인 이메일입니다.")
        return input_email
    
    def validate_phone_number(self, input_phone_number):
        if User.objects.filter(phone_number=input_phone_number).exists():
            raise serializers.ValidationError("이미 사용 중인 핸드폰 번호입니다.")
        return input_phone_number
