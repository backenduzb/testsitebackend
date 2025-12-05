from django.urls import path, include

urlpatterns = [
    path('tests/', include('tests.urls')),
    path('accounts/', include('accounts.urls')),
    path('scores/', include('scores.urls')),
    path('xlsx/', include('excel.urls'))
]