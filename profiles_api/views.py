from rest_framework.views import APIView
from rest_framework.response import Response


class Hello(APIView):
    """Test"""
    def get(self, request, format=None):
        an_apiview = [
            'use http methods'
        ]

        return Response({'message':'hello', 'an_apiview':an_apiview})