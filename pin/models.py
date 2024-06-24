import os
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from base.BaseModel import BaseModel
from authorization.models import User


@deconstructible
class FIleValidator:
    error_messages = {
        'invalid_extension': "Unsupported file extension.,"
    }
    valid_extensions = ['.jpg', '.jpeg', '.png', '.mp4', '.mov']

    def __call__(self, value):
        ext = os.path.splitext(value.name)[1].lower()
        if ext not in self.valid_extensions:
            raise ValidationError(self.error_messages['invalid_extension'])


class Board(BaseModel):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Tag(BaseModel):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Pin(BaseModel):
    image_or_Video = models.FileField(upload_to='pin/media/', validators=[FIleValidator()])
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    external_link = models.URLField(blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    board = models.ForeignKey(Board, on_delete=models.SET_NULL, blank=True, null=True, related_name="For_board")
    tagged_topics = models.ManyToManyField(Tag, blank=True, related_name="For_tags")

    allow_comment = models.BooleanField(default=True)
    show_similar_products = models.BooleanField(default=True)

    def __str__(self):
        return self.user
