import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from base.BaseModel import BaseModel
from .utils import pronouns_validator, otp_code_generator


class Pronouns(BaseModel):
    name = models.CharField(max_length=20, validators=[pronouns_validator])

    def __str__(self):
        return self.name


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True, blank=True, null=True)
    email = models.EmailField(unique=True)

    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    pronouns = models.ForeignKey(Pronouns, on_delete=models.SET_NULL, blank=True, null=True)
    website_url = models.URLField(blank=True, null=True)

    private_profile = models.BooleanField(default=False)
    search_privacy = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.email


class OTP(BaseModel):
    otp_key = models.UUIDField(default=uuid.uuid4())
    otp_code = models.IntegerField(default=otp_code_generator)
    otp_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.created_at)
