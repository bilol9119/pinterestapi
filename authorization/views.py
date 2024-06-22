from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from django.contrib.auth.hashers import make_password

from .models import User
from .serializers import UserSerializer


class AuthenticationViewSet(ViewSet):
    def token(self, request, *args, **kwargs):
        data = request.data
        user = User.objects.filter(username=data.get('username')).first()
        if not user:
            return Response(data={"error": "user not found ", 'ok': False},
                            status=status.HTTP_404_NOT_FOUND)

        if not user.is_verified:
            return Response(data={"Error": "user is not verified", 'ok': False},
                            status=status.HTTP_400_BAD_REQUEST)

        if user.check_password(data.get('password')):
            token = RefreshToken.for_user(user)
            return Response(data={'access': str(token.access_token),
                                  'refresh': str(token)}, status=status.HTTP_200_OK)
        return Response(data={"error": "password is incorrect", 'ok': False},
                        status=status.HTTP_400_BAD_REQUEST)
