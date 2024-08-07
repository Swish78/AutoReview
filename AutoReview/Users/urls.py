from django.urls import path
from .views import GoogleLogin


urlpatterns = [
    path('social/google/', GoogleLogin.as_view(), name='google_login'),
]
