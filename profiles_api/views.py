from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import viewsets

from rest_framework.authentication import TokenAuthentication

from profiles_api.serializers import HelloSerializer, UserProfileSerializer

from profiles_api.models import UserProfile

from profiles_api.permissions import UpdateOwnProfile

class Hello(APIView):

    serializer_class = HelloSerializer
    """Test"""
    def get(self, request, format=None):
        an_apiview = [
            'use http methods'
        ]

        return Response({'message':'hello', 'an_apiview':an_apiview})

    def post(self, request):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid() :
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        return Response({'method':'PATCH'})
    
    def delete(self, request, pk=None):
        return Response({'method':'delete'})

class HelloViewSets(viewsets.ViewSet):

    serializer_class = HelloSerializer


    def list(self, request):
        """Return hello msg"""
        a_viewset = [
            'uses actions list, create, retrieve, update, partial_update',
            'maps urls using routers'
        ]

        return Response({'message':'HELLO', 'viewset': a_viewset})

    def create(self, request):
        ser = self.serializer_class(data=request.data)
        if ser.is_valid():
            name = ser.validated_data.get('name')
            msg = f'hi {name}'
            return Response({msg})


class UserProfileViewSet(viewsets.ModelViewSet):
    #Handle creating and updating profiles
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)
