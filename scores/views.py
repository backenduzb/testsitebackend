from django.shortcuts import render
from .serializers import ScoreSerialzer
from .models import Score
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from tests.models import TestCase
from accounts.models import User
from scores.models import Score

class StatusView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, id):
        
        testcase = get_object_or_404(TestCase, id=id)
        score = Score.objects.filter(test=testcase, user=request.user.id).first()
        serializer = ScoreSerialzer(score)
        
        return Response(
            {'data':serializer.data},
            status=200
        )