from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
# permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from profiles_api import permissions
# Filtros y busquedas
from rest_framework import filters

# login and authentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from profiles_api import serializers
from profiles_api import models


class HelloApiView(APIView):
    """ Test APIView """
    
    serializer_class = serializers.HelloSerializer
    
    def get(self, request, format=None):
        """ Returns a list of APIView features """
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a tradictional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs'
        ]
        
        return Response({
            'message': 'Hello!',
            'an_apiview': an_apiview
        })
        
    def post(self, request):
        """ Hello message with our name """
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            
            return Response({
                'message': message,
            })
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
            
    def put(self, request, pk=None):
        """ handle updateting an object """
        return Response({
            'mesage': 'PUT'
        })
        
    def patch(self, request, pk=None):
        """ Handle a partial update of an object """
        return Response({
            'message': 'PATCH'
        })
        
    def delete(self, request, pk=None):
        """ Delete an object """
        return Response({
            'message': 'DELETE'
        })
        

class HelloViewSet(viewsets.ViewSet):
    """ Test API ViewSet """
    serializer_class = serializers.HelloSerializer
    
    def list(self, request):
        """ Return a hello message """
        
        a_viewset = [
            'Uses actions (list, create, retrive, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code'
        ]
        
        return Response({
            'message': 'Hello!',
            'an_apiview': a_viewset
        })
        
    def create(self, request):
        """ Create a new hello message """
        
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_date.get('name')
            message = f'Hello {name}!'
            return Response({
                'message': message
            })
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
            
    def retrieve(self, request, pk=None):
        """Handle getting an object by an ID """
        return Response({
            'http_method': 'GET'
        })
        
    def update(self, request, pk=None):
        """ handle updating an object """
        return Response({
            'http_method': 'PUT'
        })
        
    def partial_update(self, request, pk=None):
        """ handle updating part of an object """
        return Response({
            'http_method': 'PATCH'
        })
        
    def destroy(self, request, pk=None):
        """Handle removing an object """
        return Response({
            'http_method': 'DELETE'
        })
        
class UserProfileViewSet(viewsets.ModelViewSet):
    """ Handle creating and updating profile """
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    # Auth
    authentication_classes = (TokenAuthentication,)
    permission_classes  = (permissions.UpdateOwnProfile,)
    # busquedas
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')
    
class UserLoginApiView(ObtainAuthToken):
    """ Handle creating user authentication tokens """
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    

class ProfileFeedViewSet(viewsets.ModelViewSet):
    """ Handle creating and updating profile Feed """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (
        permissions.UpdateOwnFeedProfile,
        IsAuthenticated,
    )
    serializer_class = serializers.ProfileFeedSerializer
    queryset = models.ProfileFeed.objects.all()
    
    def perform_create(self, serializer):
        """ Sets the user profile to logged in user """
        serializer.save(user_profile=self.request.user)