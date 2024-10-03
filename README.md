# Django Project Structure - Overview

Django é um framework web escrito em Python, conhecido por sua simplicidade e "baterias incluídas", o que significa que ele vem com muitas funcionalidades prontas para uso. Esta documentação explicará a estrutura típica de um projeto Django.

## Estrutura Geral de Pastas e Arquivos

Um projeto Django geralmente segue a seguinte estrutura de diretórios:

```
my_project/
│
├── my_project/         # Diretório principal do projeto (configurações do projeto)
│   ├── __init__.py     # Arquivo de inicialização do Python
│   ├── asgi.py         # Configuração para ASGI (Asynchronous Server Gateway Interface)
│   ├── settings.py     # Configurações globais do projeto
│   ├── urls.py         # Arquivo de roteamento de URLs do projeto
│   ├── wsgi.py         # Configuração para WSGI (Web Server Gateway Interface)
│
├── my_app/             # Diretório de uma aplicação Django
│   ├── migrations/     # Diretório de migrações de banco de dados
│   ├── __init__.py     # Arquivo de inicialização do Python
│   ├── admin.py        # Configurações do admin (interface de administração)
│   ├── apps.py         # Configurações da aplicação
│   ├── models.py       # Definição de modelos de banco de dados
│   ├── tests.py        # Testes automatizados para a aplicação
│   ├── urls.py         # Roteamento de URLs da aplicação
│   ├── views.py        # Lógica de controle da aplicação (funcionalidade das rotas)
│
├── manage.py           # Script para gerenciar o projeto (rodar servidor, criar migrações, etc.)
├── db.sqlite3          # Banco de dados SQLite padrão (pode variar conforme o SGBD escolhido)
├── static/             # Arquivos estáticos (CSS, JavaScript, imagens, etc.)
├── templates/          # Arquivos de template HTML usados para renderizar páginas dinâmicas
└── requirements.txt    # Arquivo de dependências do projeto
```

## Explicação dos Principais Componentes

### 1. **manage.py**
Este é um script de linha de comando que permite interagir com o projeto Django. Com ele, você pode executar comandos para rodar o servidor, aplicar migrações de banco de dados, criar novos aplicativos e muito mais.

**Exemplo de uso:**
```bash
python manage.py runserver   # Rodar o servidor local
python manage.py migrate     # Aplicar migrações de banco de dados
```

### 2. **my_project/** (Pasta de Configuração do Projeto)

- **`__init__.py`**: Arquivo usado para marcar o diretório como um módulo Python.
- **`settings.py`**: Contém as configurações do projeto, como configurações de banco de dados, diretórios de arquivos estáticos e templates, aplicativos instalados, configurações de segurança e muito mais.
- **`urls.py`**: Define o roteamento principal das URLs. Aqui, você mapeia URLs para as views que vão processá-las.
- **`wsgi.py`**: Usado para a implantação em servidores que suportam o padrão WSGI (ex: Gunicorn, uWSGI).
- **`asgi.py`**: Usado para a implantação em servidores assíncronos que suportam o padrão ASGI (ex: Daphne).

### 3. **my_app/** (Pasta de Aplicação Django)

Django segue uma estrutura modular, onde cada aplicação dentro do projeto tem seu próprio conjunto de responsabilidades. 

- **`models.py`**: Define os modelos (classes) que representam as tabelas do banco de dados. Cada modelo tem campos que são automaticamente mapeados para colunas no banco de dados.
  
  **Exemplo:**
  ```python
  from django.db import models

  class Post(models.Model):
      title = models.CharField(max_length=100)
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
  ```

- **`views.py`**: Contém a lógica de controle da aplicação. As views processam as requisições HTTP e retornam uma resposta (normalmente renderizando uma página ou retornando JSON).

  **Exemplo:**
  ```python
  from django.http import HttpResponse

  def index(request):
      return HttpResponse("Hello, World!")
  ```

- **`urls.py`**: Arquivo que mapeia as URLs da aplicação para as views correspondentes.

  **Exemplo:**
  ```python
  from django.urls import path
  from . import views

  urlpatterns = [
      path('', views.index, name='index'),
  ]
  ```

- **`admin.py`**: Configura a interface de administração para gerenciar os dados do projeto. Aqui você registra os modelos que deseja ver no admin.

  **Exemplo:**
  ```python
  from django.contrib import admin
  from .models import Post

  admin.site.register(Post)
  ```

- **`migrations/`**: Pasta onde ficam as migrações de banco de dados geradas automaticamente. As migrações são usadas para criar, alterar ou remover tabelas no banco de dados de acordo com as mudanças nos modelos.

- **`apps.py`**: Contém a configuração da aplicação. Por exemplo, o nome da aplicação pode ser definido aqui.

### 4. **static/** e **templates/**
- **`static/`**: Diretório para armazenar arquivos estáticos, como CSS, JavaScript e imagens. Estes arquivos são servidos diretamente para o cliente.
- **`templates/`**: Diretório onde são armazenados os arquivos de template HTML. Estes templates são renderizados pelas views para exibir páginas dinâmicas ao usuário.

### 5. **db.sqlite3** (ou outro banco de dados)
O arquivo `db.sqlite3` é o banco de dados SQLite padrão criado automaticamente por Django, mas você pode configurar outros bancos de dados no `settings.py`, como PostgreSQL, MySQL, ou outros.

### 6. **requirements.txt**
Lista de dependências do projeto. Este arquivo é útil para instalar todas as bibliotecas necessárias ao projeto de forma automatizada usando o `pip`.

**Exemplo:**
```
Django==4.0
djangorestframework==3.13.1
```

## Fluxo de Trabalho Básico em Django

1. **Definir Modelos**: Criar classes no `models.py` que representam os dados que deseja armazenar no banco de dados.
2. **Criar e Aplicar Migrações**: Rodar `python manage.py makemigrations` e `python manage.py migrate` para gerar e aplicar as migrações que criarão as tabelas no banco de dados.
3. **Criar Views e URLs**: Implementar a lógica de processamento de requisições no `views.py` e mapear as URLs correspondentes no `urls.py`.
4. **Criar Templates**: Usar templates HTML no diretório `templates/` para renderizar as páginas web.
5. **Testar**: Criar testes em `tests.py` e rodar `python manage.py test` para garantir que sua aplicação funciona corretamente.

---

Esse é um resumo básico da estrutura do Django. Para mais informações, consulte a [documentação oficial do Django](https://docs.djangoproject.com/en/stable/).

--- 