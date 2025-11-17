from django.urls import path
from . import views

urlpatterns = [
    path('score/<int:id>/', views.StatusView.as_view(), name="score")
]