from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class Hello_World(APIView):
    def get(self,request):
        return Response({'message':'Hello World'},status=status.HTTP_200_OK)