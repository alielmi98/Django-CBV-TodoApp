from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.authtoken.views import ObtainAuthToken
from . import views
app_name="api-v1"


urlpatterns=[
    #registration
    path('registration/',views.RgistrationApiView.as_view(),name='registration/'),
    # change password
    path("change-password/",views.ChangePasswordApiView.as_view(),name="change-password"),
    #login Token
    path("token/login/", ObtainAuthToken.as_view(), name="token-login"),
    path("token/logout/", views.CustomDiscardAuthToken.as_view(), name="token-discard"),
    #login jwt
    path('jwt/create/', TokenObtainPairView.as_view(), name='jwt-create'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),
    
]