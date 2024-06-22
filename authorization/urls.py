from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    # path('token/', ),
    path('token/refresh', TokenRefreshView.as_view()),
]
