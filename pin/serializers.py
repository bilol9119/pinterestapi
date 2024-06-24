from rest_framework import serializers
from .models import Pin, Board


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ('id', 'name', 'collaborators', 'description', 'keep_secret')


