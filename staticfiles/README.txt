Pré requisitos:

Instalação do Python
Instalação do Django
Configuração de Ambiente Virtual
Instalando o Python
Para instalar o Python acesse: https://python.org/downloads/. Verifique a versão do pip, através do comando pip --version, caso não esteja disponível faça o download pelo https://bootstrap.pypa.io/get-pip.py Se a versão instalada estiver atualizada, você pode atualiza-la através do comando :

$python -m pip install --upgrade pip
Para intalação do Django execute o comando abaixo no prompt de comando (cmd)
$ python -m pip install Django
Para instalar uma versão do Django fornecida pela sua distribuição do sistema operacional, digite o comando abaixo no prompt de comando

$sudo apt-get install python-django
Configurando ambiente virtual (cmd) Para criação do ambiente virtual execute os comandos abaixo no cmd.
$python .manage.py -m venv venv
Para ativar o ambiente virtual

.\venv\Scripts\activate
Das dependências necessárias para execução do projeto:
Execução dos comandos para população tabelas de: localização (cidade e estado), grupos de alimentos e grupos de usuários.

Instalação de APPs utilizados no projeto

Populando as tabelas contidas no projeto A tabela de localidades será populada através do comando:

$python manage.py populate_locations
O comando utilizado para popular a tabela de grupos de alimentos:

$python manage.py populate_food
Já a tabela de grupos de usuários será populada com a utilização do comando

$python manage.py populate_create_groups
Instalação dos apps utilizados no projeto cpf_field
 $pip3 install django-cpf 
nested_admin

 $pip3 install django-nested-admin 
smart_selects

 $pip3 install django-smart-selects 
Para criar super usuário :
$python manage.py createsuperuser
Para migrar os dados para BD :
$python manage.py  makemigrations
sequido por :

$python manage.py migrate
Iniciar o servidor
$python manage.py runserver
Acesso ao projeto
http://127.0.0.1:8000/admin/