from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from profiles_api import permissions
from profiles_api import serializers
from profiles_api import models

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating UserProfiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializerPut

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
            'Uses HTTP methods as functions',
            'Is similiar to a traditional Django View',
            'Gives you most control over the application logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'Hello World!', 'an_apiview': an_apiview})


    def post(self, request):
        """Sample post test method"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            print("Entered Post request with msg "+message)
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Sample put test method"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'PUT: Hello {name}'
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def patch(self, request, pk=None):
        """Sample patch test method"""
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """Test ViewSet Api"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return list of values"""

        a_viewset = [
            'Invoked by get method',
            'Get the list of data',
            'Provides more functionality with less code'
        ]
        return Response({'message':'Hello World!', 'a_viewset':a_viewset})

    def create(self, request):
        """Sample post test method using create in viewsets"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def update(self, request, pk=None):
        """Sample put test method using viewsets"""
        return Response({'method':'PUT'})

    def partial_update(self, request, pk=None):
        """Sample patch test method using viewsets"""
        return Response({'method':'PATCH'})

    def destroy(self, request, pk=None):
        """Delete an object using viewsets"""
        return Response({'method':'DELETE'})
