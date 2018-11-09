from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserSerializer


class CheckStudent(APIView):
    def get(self, request):
        # Check user is exist or not
        user_list = User.objects.all()
        ser = UserSerializer(user_list, many=True)
        data = {'result': ser.data}
        return Response(data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "result": "success"
                }
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = {
                "result": "faild"
                }
            return Response(data)


def home(request):
    return render(request, 'user_create.html')