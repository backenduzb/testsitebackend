from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.AllTestCaseView.as_view(), name='all_tests'),
    path('check/', views.CheckAnswersView.as_view(), name='check_all')
]
