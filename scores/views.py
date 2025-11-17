from django.shortcuts import render
from .serializers import ScoreSerialzer
from .models import Score
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from tests.models import TestCase
from accounts.models import User

class StatusView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, id):
        
        user_scores = get_object_or_404(User, id=request.user.id)
        testcase = get_object_or_404(TestCase, id=id)
        score = user_scores.scores.get(test=testcase)
        serializer = ScoreSerialzer(score)
        
        return Response(
            {'data':serializer.data},
            status=200
        )