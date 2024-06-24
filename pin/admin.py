from django.contrib import admin
from .models import Pin, Board, Tag

admin.site.register(Board)
admin.site.register(Pin)
admin.site.register(Tag)

