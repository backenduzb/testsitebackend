from rest_framework import serializers 
from .models import Test, TestCase, Subject


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"

class TestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Test
        fields = '__all__'

class TestCaseSerializer(serializers.ModelSerializer):
    tests = TestSerializer(read_only=True, many=True)
    subject = SubjectSerializer(read_only=True)

    class Meta:
        model = TestCase
        fields = ['id','name','subject', 'tests']

class TestCheckerSerializer(serializers.Serializer):
    testcase_id = serializers.IntegerField()
    answers = serializers.ListField(
        child=serializers.DictField(child=serializers.CharField())
    )
