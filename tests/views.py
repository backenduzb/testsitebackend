from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import TestSerializer, TestCaseSerializer, TestCheckerSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Test, TestCase
from scores.models import Score
from django.shortcuts import get_object_or_404, get_list_or_404
from accounts.serializers import UserSerializer
from accounts.models import User

class AllTestCaseView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tests = TestCase.objects.all()
        serializer = TestCaseSerializer(tests, many=True)

        return Response(
            {'data':serializer.data},
            status=200
        )
    
    def post(self, request):
        test_id = request.data.get('test_id')
        test = get_object_or_404(TestCase, id=test_id)
        tests = get_list_or_404(Test, testcase=test)

        serializer = TestSerializer(tests, many=True)
        return Response(
            {'data':serializer.data},
            status=200
        )

class CheckAnswersView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        serializer = TestCheckerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        testcase_id = data['testcase_id']
        answers = data['answers']

        score = 0
        testcase = get_object_or_404(TestCase, id=testcase_id)
        total = 40

        for ans in answers:
            try:
                test = Test.objects.get(id=ans['test_id'], testcase=testcase)

                if test.correct_answer == ans['answer']:
                    score += float(test.test_score)

            except Test.DoesNotExist:
                pass
        
        new_score = Score.objects.create(
            test=testcase,
            score=score,
        )
        user.scores.add(new_score)
        user.save()
        serializer = UserSerializer(request.user)

        return Response({
                'user_data':serializer.data,
                'current_scores':{
                    "total": total,
                    "score": score,
                    "incorrect": total - score,
                    "percentage": f"{round((score / total) * 100, 2)}%"
        }
        }, status=200)