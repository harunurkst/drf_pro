from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User


class CheckStudent(APIView):
    def get(self, request, user_name):
        # Check user is exist or not
        is_exist = User.objects.filter(username=user_name).exists()
        data = {'result': is_exist}
        return Response(data)


def home(request):
    return render(request, 'index.html')