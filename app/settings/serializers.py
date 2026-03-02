from rest_framework import serializers
import re

from app.settings.models import Settings

class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = ['id', 'title', 'description', 'key']
    
    def validate_key(self, value):
        if not re.match(r'^[a-zA-Z0-9_-]+$', value):
            raise serializers.ValidationError('Ключ может содержать только буквы, цифры, дефисы и подчеркивания.')
        return value
    
    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError('Заголовок должен быть не менее 3 символов.')
        return value

    def validate_description(self, value):
        if len(value) < 10:
            raise serializers.ValidationError('Описание должно быть не менее 10 символов.')
        return value

    
        

