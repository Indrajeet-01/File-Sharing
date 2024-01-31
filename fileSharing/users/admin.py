from django.contrib import admin
from .models import UserAccount

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email','is_ops', 'is_staff', 'is_client')
    list_editable = ( 'is_ops','is_staff', 'is_client')

admin.site.register(UserAccount, UserAdmin)

# Register your models here.
