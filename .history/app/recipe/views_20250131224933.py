"""Views for recipe APIs"""

from rest_framework import (
    viewsets,mixins,
    )
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import (
    Recipen,Tag,
    )
from recipe import serializers

class RecipeViewSet(viewsets.ModelViewSet):
    """View for manage recipe APIs."""

    serializer_class = serializers.RecipeDetailSerializer
    queryset = Recipe.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrive recipe for authenticated user."""

        return self.queryset.filter(user=self.request.user).order_by('-id')


    def get_serializer_class(self):
        """Return recipe serializer for authenticated user."""

        if self.action == 'list':
            return serializers.RecipeSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        """Create New Recipe"""
        serializer.save(user=self.request.user)

class TagViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """Manage tags in the database."""
    serializer_class = serializers.TagSerializer
    queryset = Tag.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_class = [IsAuthenticated]

    def get_queryset(self):
        """Filter queryset to authenticated user."""
        return self.queryset.filter(user=self.request.user).order_by('-name')