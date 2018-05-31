# usuario
App Django para cadastrar e logar usuários de forma fácil

### Como usar 

1. clone o repositorio para dentro de seu projeto Django
2. Instale a app
3. Inclua as rotas ao seu projeto
4. Defina a pagina de sucesso ao se logar no sistema
5. Crie as tabelas se já não estiver criado
6. Rode os tests

```bash 
git clone https://github.com/eltonjncorreia/usuario.git
```


```bash 
INSTALLED_APPS = [
    ...

    'usuario',
]
```

### Inclua as rotas

Você pode definir a rota que quiser desde que inclua o `usuario.urls`

```bash

from django.urls import path, include

urlpatterns = [
    ...
    path('', include('usuario.urls')),
]

```


### Definir pagina de sucesso

1. localize arquivo `page_success.py` dentro de App `Usuario`
2. Defina na variavel global o caminho de sucesso ao usuario se logar"

```bash 
SUCESSO = 'core:home' 
```
### Defina no arquivo index.html linha 54 o mesmo local que definiu para pagina de sucesso
##### A pasta esta no endereço:  

``` 
templates / usuario / index.html 

<a href="{% url 'core:home' %}" class="btn btn-info">Entrar</a> 
```

### Por ultimo crie as tabelas

```bash
python manage.py migrate

```

### Rode os tests

```bash
python manage.py test
```
