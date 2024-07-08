from django.urls import path
from .views import RegisterView, CurrentUserView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)



urlpatterns = [
    path('register/', RegisterView.as_view(), name='user_register_view'),
    path('currentuser/', CurrentUserView.as_view(), name='current_user_view'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
