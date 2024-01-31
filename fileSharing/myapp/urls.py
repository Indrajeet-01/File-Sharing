
from django.urls import path
from .views import FileUploadView, FileListView, FileDownloadView

urlpatterns = [
    path('upload/', FileUploadView.as_view(), name='file-upload'),
    path('files/', FileListView.as_view(), name='file-list'),
    path('download/<int:file_id>/', FileDownloadView.as_view(), name='file-download'),
    # Add more URL patterns as needed for other views/APIs
]