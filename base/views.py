from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Email
from .serializers import EmailSerializer


class EmailReceiver(APIView):
    def post(self, request, website, format=None):
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
