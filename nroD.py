


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


''''''





