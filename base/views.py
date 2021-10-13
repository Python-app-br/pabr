from django.shortcuts import render
from base.serializers import ArtigosSerializer
from rest_framework import viewsets, permissions
from base.models import Artigos
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class ArtigosViewSet(viewsets.ModelViewSet):
  queryset = Artigos.objects.all()
  serializer_class = ArtigosSerializer
  permission_classes = [permissions.IsAuthenticated]
  filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
  filterset_fields = ['titulo', 'tag']
  search_fields = ['titulo', 'tag']
  ordering = ['-titulo']
  ordering_fields = [
        'titulo',
        'tag']

