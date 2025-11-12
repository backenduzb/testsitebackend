from django.contrib import admin
from .models import Test, TestCase, Subject

# Register your models here.

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ['testcase']

@admin.register(TestCase)
class TestCaseAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name']