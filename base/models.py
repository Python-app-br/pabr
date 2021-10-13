from django.db import models

import uuid
# model. py base.

class Artigos(models.Model):
  SETOR_CHOICES = [
    ('django', 'Django'), ('python', 'Python'), ('git', 'Git')
  ]

  id = models.UUIDField(
    primary_key=True,
    default=uuid.uuid4,
    null=False,
    blank=True)

  titulo = models.CharField(
    max_length=120,
    null=False,
    blank=False)

  conteudo = models.CharField(
    max_length=120,
    null=False,
    blank=False)

  autor = models.CharField(
    max_length=120,
    null=False,
    blank=False)

  tag = models.CharField(
    max_length=30,
    null=False,
    blank=False,
    choices=SETOR_CHOICES)

  links = models.CharField(
    max_length=120,
    null=False,
    blank=False)


