from django.urls import path
from . import views

urlpatterns = [
    path('<str:subject>/', views.FileDownloadView().as_view(), name="xlsx_download"),
]