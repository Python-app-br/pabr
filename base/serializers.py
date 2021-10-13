from rest_framework import serializers
from base.models import Artigos

class ArtigosSerializer(serializers.ModelSerializer):
  class Meta:
    model = Artigos
    fields = [
      'id',
      'titulo',
      'conteudo',
      'autor',
      'tag',
      'links'
    ]