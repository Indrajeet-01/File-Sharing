from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    file_type = models.CharField(max_length=10, choices=[('pptx', 'PPTX'), ('docx', 'DOCX'), ('xlsx', 'XLSX')])
    uploaded_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.file.name} - {self.user.email}"
