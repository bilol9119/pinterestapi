from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .models import Pin, Board
from .serializers import BoardSerializer


class BoardViewSet(ViewSet):
    def create_board(self, request, *args, **kwargs):
        data = request.data
        data['user'] = request.user
        serializer = BoardSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": serializer.data}, status.HTTP_201_CREATED)
        return Response({"detail": "enter valid data"}, status.HTTP_400_BAD_REQUEST)

