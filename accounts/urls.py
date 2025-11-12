from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.CutomLoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('me/', views.GetUserInfoView.as_view(), name='user_info'),
]