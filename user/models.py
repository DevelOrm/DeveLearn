from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_superuser(self, user_id, password, phone_number, **extra_fields):
        user = self.model(
            user_id = user_id,
            nickname = '관리자',
            email = 'develorm@gmail.com',
            phone_number = phone_number,
            **extra_fields
        )
        user.is_admin = True
        user.set_password(password)
        user.save()
        return user

class User(AbstractBaseUser):
    objects = UserManager()
    user_id = models.CharField(max_length=20, unique=True)
    nickname = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=128, unique=True)
    phone_number = models.CharField(max_length=14, unique=True)
    profile_image = models.ImageField(blank=True, null=True)
    joined_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_teacher = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    # password, last_login, is_active 기본 상속

    USERNAME_FIELD = "user_id"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["phone_number"]
    
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
