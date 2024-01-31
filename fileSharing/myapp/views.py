from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from django.http import FileResponse, HttpResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mail
from .serializers import FileSerializer
from .models import File

class FileUploadView(APIView):
    

    def post(self, request):
        if not request.user.is_ops:
            return Response({'error': 'Only Ops User can upload files'}, status=status.HTTP_403_FORBIDDEN)

        file_serializer = FileSerializer(data=request.data)

        if file_serializer.is_valid():
            # Set the user to the current Ops User during serializer save
            file_instance = file_serializer.save(user=request.user)

            # Generate the secure download URL and save it
            file_instance.secure_download_url = file_instance.generate_download_url()
            file_instance.save()

            return Response({'success': 'File uploaded successfully'}, status=status.HTTP_201_CREATED)

        return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class FileListView(ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    

class FileDownloadView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, file_id):
        # Fetch the file based on the provided file_id
        file_instance = File.objects.get(pk=file_id)

        # Serve the file for download using Django's FileResponse
        file_path = file_instance.file.path
        response = FileResponse(open(file_path, 'rb'))
        response['Content-Disposition'] = f'attachment; filename="{file_instance.file.name}"'

        # Send an email to the client user with the download link
        download_url = f'http://localhost:8000/api/download/{file_instance.id}/'
        send_email_to_client(request.user.email, download_url)

        return response

# This function is just a placeholder for demonstration purposes.
def send_email_to_client(email, download_url):
    subject = 'File Download Link'
    message = f'Click on the following link to download your file: {download_url}'
    from_email = 'your@example.com'  # Replace with your email
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)