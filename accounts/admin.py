from django.contrib import admin, messages
from .models import User, Class
from django.contrib.auth.models import Group


admin.site.unregister({Group})

@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'is_staff', 'is_active','full_name', 'class_name']
    
@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ['id','name']