from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


def home_view(request):
    return JsonResponse({"message": "Welcome to the Home Page!"})


def about_view(request):
    return JsonResponse({"message": "This is the About Page."})


class HomeAPIView(APIView):
    def get(self, request):
        data = {"message": "Welcome to the Home API!"}
        return Response(data, status=status.HTTP_200_OK)


class AboutAPIView(APIView):
    def get(self, request):
        data = {"message": "This is the About API."}
        return Response(data, status=status.HTTP_200_OK)
