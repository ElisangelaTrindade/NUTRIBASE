This is my readme


# Pré requisitos:
1. Instalação do Python
2. Instalação do Django;
3. Configuração de Ambiente Virtual


1. Instalando o Python
Para instalar o Python acesse: https://python.org/downloads/. 
Verifique a versão do pip, através do comando pip --version, caso não esteja disponível faça o download pelo https://bootstrap.pypa.io/get-pip.py
Instale. Se a versão instalada estiver atualizada, você pode atualiza-la através do comando :
```bash $python -m pip install --upgrade pip ```

2. Para intalação do Django execute o comando abaixo no prompt de comando (cmd)
```bash  $ python -m pip install Django ```
2.1 Para  instalar uma versão do Django fornecida pela sua distribuição do sistema operacional, digite o comando abaixo no prompt de comando 
``` bash $sudo apt-get install python-django ```

3. Configurando ambiente virtual (cmd)
Para criação  do ambiente virtual execute os comandos abaixo no cmd.
```bash $python .manage.py -m venv venv  ```
```bash .\venv\Scripts\activate ```

# Das dependências necessárias para execução  do projeto:
1. Execução dos comandos para população tabelas de: localização (cidade e estado), grupos de alimentos e grupos de usuários.
2. Instalação de APPs utilizados no projeto 

Populando as tabelas contidas no projeto
A tabela de localidades será populada através do comando ```bash $python manage.py populate_locations ```
O comando ```bash $python manage.py populate_food ``` deverá ser utilizado para popular a tabela de grupos de alimentos
Já a tabela de grupos de usuários será populada com a utilização do comando ```bash $python manage.py populate_create_groups ```

2. Instalação dos apps utilizados no projeto
    'cpf_field' -  $pip3 install django-cpf 
    'nested_admin' - $pip3 install django-nested-admin 
    'smart_selects'-  $pip3 install django-smart-selects 

________________________________________________________________

# Pre requirements:
1. Python Installation
2.Installation of Django;
3.Configuration of Virtual Environment


1. Installing Python
To install Python go to: https://python.org/downloads/.
Check the pip version using the pip --version command, if it is not available, download it from https://bootstrap.pypa.io/get-pip.py
Install. If the installed version is up to date, you can upgrade it via the command ```bash  python -m pip install --upgrade pip ```

2. To install Django run the command below at the command prompt (cmd)
```bash
$ python -m pip install Django
```
2.1 To install a version of Django provided by your operating system distribution, type the command below at the command prompt
```bash
$sudo apt-get install python-django
```
3. Setting up virtual environment (cmd)
To create the virtual environment run the commands below in cmd.
```bash
 $python .manage.py -m venv venv 
```
```bash
.\venv\Scripts\activate
```

# The dependencies needed to carry out the project:
1. Execution of commands for population tables of: food groups, user groups and location (city and state)
2. Installation of APPs used in the project

1. Populating the tables contained in the project
The ```bash $python manage.py populate_food ``` command should be used to populate the food groups table
The location table wi ll be populated via the command ```bash $python manage.py populate_locations ```
The user groups table will be populated using the ```bash $python manage.py populate_create_groups ``` command

2. Installation of apps used in the project
    'cpf_field' - ```bash $pip3 install django-cpf ```
    'nested_admin' - ```bash $pip3 install django-nested-admin ```
    'smart_selects'- ```bash $pip3 install django-smart-selects ```
