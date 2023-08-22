from django.db import models
from django.core.validators import RegexValidator
# from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, user_id, password, user_name, email, phone_number, **extra_fields):
        if not email:
            raise ValueError("이메일이 없습니다.")
        
        user = self.model(
            user_id = user_id,
            email = self.normalize_email(email),
            user_name = user_name,
            phone_number = phone_number,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, user_id, password, user_name, email, **extra_fields):
        user = self.model(
            user_id = user_id,
            email = self.normalize_email(email),
            user_name = user_name,
            **extra_fields
        )
        user.is_admin = True
        user.set_password(password)
        user.save()
        return user

class User(AbstractBaseUser):
    objects = UserManager()
    user_id = models.CharField(max_length=20, unique=True)
    user_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=128, unique=True)
    phone_number_regex = RegexValidator(regex=r'^01([0|1|6|7|8|9]?)-?([0-9]{3,4})-?([0-9]{4})$')
    phone_number = models.CharField(validators=[phone_number_regex], max_length=11, blank=True)
    profile_image = models.ImageField(blank=True)
    joined_date = models.DateTimeField(auto_now_add=True)
    is_teacher = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    # password, last_login, is_active 기본 상속

    USERNAME_FIELD = "user_id"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["user_name", "email"]
    
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