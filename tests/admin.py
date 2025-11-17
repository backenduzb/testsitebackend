from django.contrib import admin
from .models import Test, TestCase, Subject, Ball

# Register your models here.


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ['id','testcase']

@admin.register(Ball)
class BallAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'score']


@admin.register(TestCase)
class TestCaseAdmin(admin.ModelAdmin):
    list_display = ['id','name']

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['id','name']