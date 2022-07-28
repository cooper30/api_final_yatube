from rest_framework import permissions, status


class IsAuthorOrReadOnly(permissions.BasePermission):
    message = "Вы не можете изменить объект, созданный другим пользователем!"
    code = status.HTTP_403_FORBIDDEN

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user
