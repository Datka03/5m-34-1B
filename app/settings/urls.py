from django.urls import path
from app.settings.views import HelloAPIView, SettingsListAPIView, SettingsCreateAPIView

urlpatterns = [
    path("", HelloAPIView.as_view(), name='hello'),
    path("settings", SettingsListAPIView.as_view(), name='settings-list'), 
    path("settings-create", SettingsCreateAPIView.as_view(), name='settings-create')
]
