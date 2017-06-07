from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from . import models

# Create your views here.
# we are now using viewsets rather the original apiview

## Hello test view set
class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet """
    serializer_class = serializers.HelloSerializer

    def list(self,request):
        """Return a Hello message. """
        an_apiviewset = [
            'Uses actions (list, create,retrieve,update,partial_update)'
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code'
        ]
        return Response({'message':'Hello','an_apiviewset':an_apiviewset})

    def create(self,request):
        """create a new hello message."""
        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        """Handles getting an object by its ID"""

        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        """Handles updating an object by its ID"""

        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        """Handles partial updating an object by its ID"""

        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        """Handles removing an object by its ID"""

        return Response({'http_method':'DELETE'})

## simple user profile view set
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creates, createing and updateing profiles. """
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
