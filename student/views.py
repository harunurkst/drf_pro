from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Board, StudentInfo
from .serializers import BoardSerializer, StudentSerializer


class Student(APIView):
    def get(self, request):
        # Check user is exist or not
        board_list = Board.objects.all()
        board = BoardSerializer(board_list, many=True)
        data = {'result': board.data}
        return Response(data)

    def post(self, request):
        print('working')
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            roll = serializer.validated_data['roll']
            board = serializer.validated_data['board']
            student = StudentInfo.objects.get(roll=roll)
            print(student)
            data = {'name': student.name,
                    'roll': student.roll,
                    'father': student.father,
                    'gpa': student.gpa,
                    'board': student.board.name}
            return Response(data)
        else:
            print(serializer.errors)
            data = {'result': 'failed'}
            return Response(data)

def students(request):
    return render(request, 'student.html')