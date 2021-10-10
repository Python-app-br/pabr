


'''primeiro exemplo SECRET_KEY'''

# Read SECRET_KEY from an environment variable
import os
SECRET_KEY = os.environ['SECRET_KEY']
# OR
# Read secret key from a file
with open('/etc/secret_key.txt') as f:
    SECRET_KEY = f.read().strip()

'''mudar settings.py SECRET_KEY'''

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'cg#p$g+j9tax!#a3cup@1$8obt2_+&k3q+pmu)5%asj6yjpkag'
import os
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'cg#p$g+j9tax!#a3cup@1$8obt2_+&k3q+pmu)5%asj6yjpkag')

'''comente o DEBUG original e acrescente -- settings.y'''

DEBUG = os.environ.get('DJANGO_DEBUG', '') != 'False'

'''Você pode definir a variável de ambiente como False, emitindo o seguinte comando:'''
export DJANGO_DEBUG=False

'''criar repositorio github'''

Visite https://github.com/ e crie uma conta.
Depois de fazer login, clique no link + na barra de ferramentas superior e selecione Novo repositório.
Preencha todos os campos deste formulário. Embora não sejam obrigatórios, são fortemente recomendados.
Insira um novo nome de repositório (por exemplo, django_local_library) e uma descrição (por exemplo, "Site da biblioteca local escrito em Django".
Escolha Python na lista de seleção Add .gitignore.
Escolha sua licença preferida na lista de seleção Adicionar licença.
Marque Inicializar este repositório com um README.
Pressione Criar repositório.
Clique no botão verde "Clonar ou baixar" na sua nova página de repositório.
Copie o valor da URL do campo de texto dentro da caixa de diálogo que aparece (deve ser algo como: https://github.com/ <your_git_user_id> /django_local_library.git).

'''clonar url'''
https://github.com/Python-app-br/pabr.git


'''instalar o git'''

'''Para obter a versão estável mais recente para o seu lançamento do Debian / Ubuntu'''

apt-get install git

'''Para o Ubuntu, este PPA fornece a versão upstream estável mais recente do Git'''

add-apt-repository ppa:git-core/ppa 
apt update
apt install git


'''copiar ou criar projeto app django'''
As etapas finais são copiar seu aplicativo
para o diretório local do projeto e, em seguida,
adicionar (ou "push", no jargão git) 
o repositório local ao seu repositório Github remoto:


'''adicionar arquivos a area de teste'''

Abra um prompt de comando / terminal e use o comando add 
para adicionar todos os arquivos ao git. Isso adiciona os arquivos
que não são ignorados pelo arquivo .gitignore à "área de teste".

git add -A


'''checar status'''
git status

'''tudo ok. envie os arquivos para seu repositório'''
git commit -m "First version of application moved into github"

'''sincronizar enviando repo local para o repo remoto github'''

git push origin master

'''fazer backup do projeto'''

'''configurar app django para o heroku'''
'''criar arquivo sem extenção Procfile na raiz do git repo local'''
'''adicionar ao Procfile'''

web: gunicorn locallibrary.wsgi --log-file -

'''instalar gunicorn'''
pip3 install gunicorn

'''instalar dj-database-url'''
pip3 install dj-database-url

'''configurar database -- settings.py'''
# Heroku: Update database configuration from $DATABASE_URL.
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

'''usaremos SQLite mas é possivelinstalar as dependencias Postgres localmente'''

sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib
pip3 install psycopg2-binary

'''configurar variaveis settings.py'''

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

# The absolute path to the directory where collectstatic will collect static files for deployment.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# The URL to use when referring to static files (where they will be served from)
STATIC_URL = '/static/'


'''instalar whitenoise'''
pip3 install whitenoise

'''configurar MIDDLEWARE e adicione o WhiteNoiseMiddleware abaixo de SecurityMiddleware:'''

'whitenoise.middleware.WhiteNoiseMiddleware',


'''diminuir tamanho dos arquivos estaticos '''

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

'''criar requirements.txt'''
pip3 freeze > requirements.txt
'''conteudo'''
dj-database-url==0.5.0
Django==2.1.5
gunicorn==19.9.0
psycopg2-binary==2.7.7
whitenoise==4.1.2

'''criar arquivo na raiz runtime.txt'''
python-3.7.0


#HEROKU 

heroku help
'''criar site heroku'''
heroku create

'''enviar projeto app'''
git push heroku master



