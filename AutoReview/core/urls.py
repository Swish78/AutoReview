from django.urls import path
from .views import home_view, about_view, HomeAPIView, AboutAPIView

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('api/home/', HomeAPIView.as_view(), name='home_api'),
    path('api/about/', AboutAPIView.as_view(), name='about_api'),
]
