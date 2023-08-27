from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from user.nicknameGenerator import Nickname_generator

# Create your models here.

class UserManager(BaseUserManager):
    # def create_user(self, user_id, password, email, phone_number, **extra_fields):
    #     user = self.model(
    #         user_id = user_id,
    #         email = self.normalize_email(email),
    #         nickname = Nickname_generator.roll_the_dice(),
    #         phone_number = phone_number,
    #         **extra_fields
    #     )
    #     user.set_password(password)
    #     user.save()
    #     return user
    
    def create_superuser(self, user_id, password, **extra_fields):
        user = self.model(
            user_id = user_id,
            nickname = '관리자',
            **extra_fields
        )
        user.is_admin = True
        user.set_password(password)
        user.save()
        return user

class User(AbstractBaseUser):
    objects = UserManager()
    user_id = models.CharField(max_length=20, unique=True)
    nickname = models.CharField(max_length=20)
    email = models.EmailField(max_length=128, blank=True, null=True)
    phone_number_regex = RegexValidator(regex=r'^01([0|1|6|7|8|9]?)-?([0-9]{3,4})-?([0-9]{4})$')
    phone_number = models.CharField(validators=[phone_number_regex], max_length=11, blank=True, null=True)
    profile_image = models.ImageField(blank=True, null=True)
    joined_date = models.DateTimeField(auto_now_add=True)
    is_teacher = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    # password, last_login, is_active 기본 상속

    USERNAME_FIELD = "user_id"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.user_id
    
    def is_superuser(self):
        return self.is_admin

    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin


    class Meta:
        db_table = "user"
        verbose_name = "user"
        verbose_name_plural = "users"