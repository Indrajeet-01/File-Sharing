
from rest_framework import serializers
from .models import File

class FileSerializer(serializers.ModelSerializer):
    secure_download_url = serializers.SerializerMethodField()

    class Meta:
        model = File
        fields = '__all__'

    def get_secure_download_url(self, obj):
        return f'http://localhost:8000/api/download/{obj.id}/'
