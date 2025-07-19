from rest_framework import permissions


class GeneroPermissionClass(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user.has_perm('generos.view_genero')
        
        if request.method == 'POST':
            return request.user.has_perm('generos.add_genero')
    
        if request.method in ['PUT', 'PATCH', 'DELETE']:
            return request.user.has_perm('generos.change_genero') or request.user.has_perm('generos.delete_genero')
        
        return False