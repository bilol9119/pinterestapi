from django.urls import path
from .views import BoardViewSet
urlpatterns = [
    path('create/board/', BoardViewSet.as_view({"post": "create_board"}))
]