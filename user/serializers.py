from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.core.exceptions import ValidationError as DjangoValidationError
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from user.models import User
from user.nicknameGenerator import Nickname_generator

class UserRegisterSerializer(RegisterSerializer):
    random_nickname = Nickname_generator.roll_the_dice()
    nickname =  serializers.CharField(default=random_nickname)
    profile_image = serializers.ImageField(allow_null=True)
    phone_number =  serializers.CharField(allow_null=True)
    is_teacher = serializers.BooleanField()

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



class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'nickname', 'email', 'phone_number', 'profile_image', 'last_login', 'joined_date', 'is_teacher']