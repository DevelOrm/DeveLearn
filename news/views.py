from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class NewsBotView(APIView):
    def post(self, request, format=None):
        data = request.data
        print(data['33'])
        return Response({'message': 'JSON data received successfully'}, status=status.HTTP_201_CREATED)
