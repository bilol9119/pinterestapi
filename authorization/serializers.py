from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email',
                  'password', 'pronouns', 'website_url', 'about',
                  'profile_photo', 'private_profile', 'search_privacy',
                  'created_at')
        extra_kwargs = {
            'password': {"write_only": True}
        }
