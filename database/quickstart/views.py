from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from .models import Pflege
from .serializers import PflegeSerializer

class PflegeView(APIView):
    def get(self, request, format=None):
        data = Pflege.objects.all()
        serializer = PflegeSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PflegeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
