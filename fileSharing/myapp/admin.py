from django.contrib import admin
from .models import File

class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'file', 'file_type', 'uploaded_at')
    search_fields = ('user__email', 'file', 'file_type')
    list_filter = ('file_type', 'uploaded_at')

admin.site.register(File, FileAdmin)