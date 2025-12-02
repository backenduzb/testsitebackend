from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import TestSerializer, TestCaseSerializer, TestCheckerSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Test, TestCase
from scores.serializers import ScoreSerialzer
from scores.models import Score
from django.shortcuts import get_object_or_404, get_list_or_404
from accounts.serializers import UserSerializer
from accounts.models import User

class AllTestCaseView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        testcases = TestCase.objects.all().order_by('-id')
        user_scores = Score.objects.filter(user=request.user)
        result = []
        completed_testcase_ids = set(user_scores.values_list('test', flat=True)) 

        for testcase in testcases:
            tests = testcase.tests.all()  
            tests_data = TestSerializer(tests, many=True).data

            testcase_completed = testcase.id in completed_testcase_ids

            testcase_data = TestCaseSerializer(testcase).data
            testcase_data['this_completed'] = testcase_completed
            result.append(testcase_data)

        return Response({'data': result}, status=200)
    
    def post(self, request):
        secure_code = request.data.get("secure_code")

        test_id = request.data.get('test_id')
        test = get_object_or_404(TestCase, id=test_id)
        tests = get_list_or_404(Test, testcase=test)
        
        if secure_code == test.secret_key:

            serializer = TestSerializer(tests, many=True)
            response = Response(
                {'data':serializer.data, 'count':len(tests)},
                status=200
            )
        else:
            response = Response(
                {'message':"hafsizlik kodi noto'g'ri kiritldi."},
                status=400
            )

        return response
        
class CheckAnswersView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        serializer = TestCheckerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        bilish = 0
        qollash = 0
        muhokama = 0

        testcase_id = data['testcase_id']
        answers = data['answers']

        qollash_count = 0
        muhokama_count = 0
        bilish_count = 0
        score = 0
        testcase = get_object_or_404(TestCase, id=testcase_id)
        all_tests_count = Test.objects.filter(testcase=testcase).count()

        for ans in answers:
            try:
                test = Test.objects.get(id=ans['test_id'], testcase=testcase)

                if test.correct_answer == ans['answer']:
                    if test.test_score.name == "Bilish":
                        bilish += float(test.test_score.score)
                        bilish_count += 1
                    if test.test_score.name == "Qo'llash":
                        qollash += float(test.test_score.score)
                        qollash_count += 1
                    if test.test_score.name == "Muhokama":
                        muhokama += float(test.test_score.score)
                        muhokama_count += 1
                    score += float(test.test_score.score)

            except Test.DoesNotExist:
                pass

        all_correct = bilish_count+qollash_count+muhokama_count
        
        new_score = Score.objects.create(
            total=all_tests_count,
            completed=all_correct,
            test=testcase,
            score=score,
            bilish=bilish,
            bilish_count=bilish_count,
            qollash=qollash,
            qollash_count=qollash_count,
            muhokama=muhokama,
            muhokama_count=muhokama_count
        )
        user.scores.add(new_score)
        user.save()
        score_serializer = ScoreSerialzer(new_score)
        serializer = UserSerializer(request.user)
        return Response({
                'user_data':serializer.data,
                'current_scores':score_serializer.data
        }, status=200)