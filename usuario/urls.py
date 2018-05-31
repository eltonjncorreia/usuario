from django.urls import path
from django.contrib.auth import views as auth_views
from .views import landingpage, validar

app_name = 'usuario'
urlpatterns = [
    path('', landingpage, name='landingpage'),
    path('login/', auth_views.login, {'template_name': 'usuario/form_login.html'}, name='login'),
    path('logout/', auth_views.logout, {'next_page': '/'}, name='logout'),
    path('validar/', validar, name='validar'),
]
