from rest_framework import serializers
from tests.serializers import TestCaseSerializer
from .models import Score

class ScoreSerialzer(serializers.ModelSerializer):
    test = TestCaseSerializer()

    class Meta:
        model = Score
        fields = '__all__'