from rest_framework import serializers
from .models import Board, StudentInfo

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'

class StudentSerializer(serializers.Serializer):
    roll = serializers.IntegerField()
    board = serializers.CharField()