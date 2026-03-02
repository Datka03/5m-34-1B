from django.urls import path
from app.settings.views import (
# 1 урок  HelloAPIView, SettingsListAPIView, SettingsCreateAPIView
    PublicSettingsListAPIView, PublicSettingsDetailAPIView, AdminSettingsListAPIView
)
urlpatterns = [
    # 1 урок
    # path("", HelloAPIView.as_view(), name='hello'),
    # path("settings", SettingsListAPIView.as_view(), name='settings-list'), 
    # path("settings-create", SettingsCreateAPIView.as_view(), name='settings-create')
    path("public-settings", PublicSettingsListAPIView.as_view(), name='public-settings-list'),
    path("public-settings/<str:key>", PublicSettingsDetailAPIView.as_view(), name='public-settings-detail'),
    path("admin-settings", AdminSettingsListAPIView.as_view(), name='admin-settings-list'),
]
