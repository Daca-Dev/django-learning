from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """ Allow user to edit their own profile """
    
    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id
    
class UpdateOwnFeedProfile(permissions.BasePermission):
    """ Allow user to edit their own feed profile """
    
    def has_object_permission(self, request, view, obj):
        """ Check if user triying to edit their own feed """
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id