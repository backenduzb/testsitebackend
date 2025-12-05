from tests.models import Test, TestCase, Subject
from django.http import FileResponse, Http404
from django.shortcuts import render
from accounts.models import User
from scores.models import Score
from .writer import make_xlsx
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.http import HttpResponseRedirect
import os

class FileDownloadView(APIView):

    permission_classes = [AllowAny]
    def get(self, request, subject):
        make_xlsx(subject)
        if os.path.exists(f"{subject}, Natijalar.xlsx"):
            return FileResponse(open(f"{subject}, Natijalar.xlsx", 'rb'), as_attachment=True, filename=f"{subject}, Natijalar.xlsx")
        else:
            raise Http404("Fayl topilmadi")
            