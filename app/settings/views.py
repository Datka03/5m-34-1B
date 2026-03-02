from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from app.settings.models import Settings
from app.settings.serializers import SettingsSerializer


# 1 урок
# class HelloAPIView(APIView):
#     def get(self, request):
#         return Response({"message" : "Hello DRF!"})

# class SettingsListAPIView(APIView):
#     def get(self, request):
#         setting = Settings.objects.all()
#         serializer = SettingsSerializer(setting, many=True)
#         return Response(serializer.data)

# class SettingsCreateAPIView(APIView):
#     def post(self, request):
#         serializer = SettingsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PublicSettingsListAPIView(APIView):
    def get(self, request):
        settings = Settings.objects.filter(is_public=True).order_by('key')
        serializer = SettingsSerializer(settings, many=True)
        return Response(serializer.data)

class PublicSettingsDetailAPIView(APIView):
    def get(self, request, key):
        settings = get_object_or_404(Settings, key=key, is_public=True)
        serializer = SettingsSerializer(settings)
        return Response(serializer.data)

class AdminSettingsListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        settings = Settings.objects.all().order_by('key')
        serializer = SettingsSerializer(settings, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SettingsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=400)