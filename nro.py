
'''roteiro criar base Django rest framework'''


'''criar diretorio raiz'''
mkdir nomediretorio
'''acessar diretorio'''
cd nomediretorio
'''criar ambiente virtual'''
python3 -m venv nome-env
'''ativar ambiente virtual'''
source nome-env/bin/activate

'''instalar Djangorestframework'''
pip install django '''opicional'''
pip install djangorestframework
'''instalar pacotes opcionais'''
pip install markdown
pip install django-filter
pip install pygments

'''criando novo projeto django REST framework no ambiente virtual venv'''
django-admin startproject nome-projeto . '''detalhe do espaço e ponto no final que muda a estrutura de diretorios'''
'''acessar diretorio do projeto'''
cd nome-projeto
'''criar app no projeto'''
django-admin startapp nome-app
'''voltar a raiz'''
cd ..
'''criar usuario inicial''' '''senha ppp111ppp111''' 
python manage.py createsuperuser --email admin@fic.com --username admin

'''paginaçao'''
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

'''adicionando rest_framework a installed_apps em /nome_projeto/settings.py'''
INSTALLED_APPS = [
    ...
    'rest_framework',
    'snippets.apps.SnippetsConfig',
]

'''criando o modelo para trabalho /snippets/models.py '''
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ['created']


'''sincronizar banco de dados pela primeira vez'''
python manage.py makemigrations snippets
python manage.py migrate

'''definir serializadores  --  criando arquivo serializers.py no diretorio da app(nome-app)'''
metodo opicional ,criar com seu editor preferido ou outros

from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance


'''definir serializadores com ModelSerializer -- mudança na Classe SnippetSerializer '''   
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance


'''Escrever visualizações regulares Django com nosso Serializer'''  
'''editar snippets/views.py'''   
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)


'''conectar visualizações -- criar arquivo -- snippets/urls.py'''
from django.urls import path
from snippets import views

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
]


'''conectar urlconf  -- no arquivo -- tutorial/urls.py '''

from django.urls import path, include

urlpatterns = [
    path('', include('snippets.urls')),
]

'''instalar httpie com pip para testes em linha de comando'''

pip install httpie

'''exemplo de teste com httpie em linha de comando'''
http http://127.0.0.1:8000/snippets/
# ou por exemplo com um id especifico
http http://127.0.0.1:8000/snippets/2/


'''objetos de solicitação -- REST Request'''

request.POST  # Só lida com dados de formulário. Funciona apenas para o método 'POST'.
request.data  # Lida com dados arbitrários. Funciona para os métodos 'POST', 'PUT' e 'PATCH'.

'''objetos de resposta -- REST Response -- que é um tipo de TemplateResponse'''

return Response(data)  # Renderiza para o tipo de conteúdo conforme solicitado pelo cliente.


'''adicionar sufixos a urls'''
def snippet_list(request, format=None):
def snippet_detail(request, pk, format=None):

'''atualizar snippets/urls.py para anexar format_suffix_patterns'''

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>', views.snippet_detail),
]
urlpatterns = format_suffix_patterns(urlpatterns)

'''apis baseadas em classes'''

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class SnippetList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SnippetDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



''' refatorar snippets/urls.py  para viasualizações baseadas em classes'''
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)

'''Usando mixins'''

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import mixins
from rest_framework import generics

class SnippetList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class SnippetDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


'''visualizações genéricas baseadas em classe'''

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics

class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

'''autenticação e permissões -- Adicionar informações ao modelo'''
'''Snippes/models.py'''

from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

#campos adicionais classe snippet
owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
highlighted = models.TextField()
#funçao adicional para classe snippet
def save(self, *args, **kwargs):
    """
    Use the `pygments` library to create a highlighted HTML
    representation of the code snippet.
    """
    lexer = get_lexer_by_name(self.language)
    linenos = 'table' if self.linenos else False
    options = {'title': self.title} if self.title else {}
    formatter = HtmlFormatter(style=self.style, linenos=linenos,
                              full=True, **options)
    self.highlighted = highlight(self.code, lexer, formatter)
    super(Snippet, self).save(*args, **kwargs)

'''apagar banco de dados e migrações'''
rm -f db.sqlite3
rm -r snippets/migrations
'''recriar banco de dados e migrações'''
python manage.py makemigrations snippets
python manage.py migrate
'''criar superusuario'''
python manage.py createsuperuser

'''adicionar representações para ususarios -- snippets/serializers.py '''
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']


'''adicionar visualizações -- snippets/views.py'''

from django.contrib.auth.models import User
from snippets.serializers import UserSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

'''referenciar as visualizações a API --- snippets/urls.py'''

path('users/', views.UserList.as_view()),
path('users/<int:pk>/', views.UserDetail.as_view()),

'''associar snippets a usuarios'''

def perform_create(self, serializer):
    serializer.save(owner=self.request.user)

'''atualizar nosso serializador -- serializers.py'''

owner = serializers.ReadOnlyField(source='owner.username')

'''adicionar  'owner' a meta classe interna -- exemplo'''

fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'owner']

'''adicionar permissões necessarias as visualizações'''
from rest_framework import permissions #modulo de visualizações

'''adicionar propriedade para os SnippetListe e SnippetDetail'''

permission_classes = [permissions.IsAuthenticatedOrReadOnly]

'''adicionar login à API Browsable -- tutorial/urls.py'''
from django.urls import path, include

'''visualizações de login e logout para a API navegável'''
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]

'''permissões de nível de objeto -- permissão personalizadas'''
'''criar novo arquivo -- snippets/permissions.py'''

from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user

'''editar permission_classespropriedade na SnippetDetailclasse de visualização'''

permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]


'''importar IsOwnerOrReadOnly na views'''
from snippets.permissions import IsOwnerOrReadOnly

'''criar um endpoint para a raiz de nossa api'''
'''usando espressção regular e o @api_view -- snippets/views.py'''

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })

'''criar endpoint para trechos destacados -- snippets/views.py'''
from rest_framework import renderers

class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

'''adicionar visualização no urlconf -- snippets/urls.py'''

path('', views.api_root),

'''e um padrao de url para os destaques snippets'''

path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view()),

'''usar Hiperlink na API'''
'''reescrever  serializadores existentes para usar hiperlinks -- snippets/serializers.py'''

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ['url', 'id', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']


'''certificar que os padrões de URL são nomeados -- snippets/urls.py'''

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

# API endpoints
urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('snippets/',
        views.SnippetList.as_view(),
        name='snippet-list'),
    path('snippets/<int:pk>/',
        views.SnippetDetail.as_view(),
        name='snippet-detail'),
    path('snippets/<int:pk>/highlight/',
        views.SnippetHighlight.as_view(),
        name='snippet-highlight'),
    path('users/',
        views.UserList.as_view(),
        name='user-list'),
    path('users/<int:pk>/',
        views.UserDetail.as_view(),
        name='user-detail')
])


'''adicionar paginação -- tutorial/settings.py'''

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

''''''


