from rest_framework import serializers 
from .models import Test, TestCase, Subject, Ball
from scores.models import Score

class BallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ball
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"

class TestSerializer(serializers.ModelSerializer):
    test_score = BallSerializer()

    class Meta:
        model = Test
        exclude = ["correct_answer"]

    
class TestCaseSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(read_only=True)
    tests_count = serializers.SerializerMethodField()
    this_completed = serializers.SerializerMethodField()

    class Meta:
        model = TestCase
        fields = ['id','name','subject', 'over_time','tests_count', 'this_completed']

    def get_this_completed(self, obj):
        user = self.context.get('user')
        if not user:
            return False
        return Score.objects.filter(user=user, test=obj).exists()
    
    def get_tests_count(self, obj):
        return obj.tests.count()

class TestCheckerSerializer(serializers.Serializer):
    testcase_id = serializers.IntegerField()
    answers = serializers.ListField(
        child=serializers.DictField(child=serializers.CharField())
    )
