from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Classroom
from .serializers import ClassroomSerializer


class ClassroomView(APIView):
    def get(self, request):
        classrooms = Classroom.objects.all()
        serializer = ClassroomSerializer(classrooms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ClassroomSerializer(data=request.data)
        if serializer.is_valid():
            classroom = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        classroom = Classroom.objects.get(pk=pk)
        classroom.delete()
        return Response({'message': 'Classroom deleted'}, status=status.HTTP_202_ACCEPTED)

    def patch(self, request, pk):
        classroom = Classroom.objects.get(pk=pk)
        serializer = ClassroomSerializer(classroom, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
