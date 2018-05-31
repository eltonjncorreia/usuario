from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import resolve_url as r, render
from .page_success import SUCESSO
from .forms import UserForm


def landingpage(request):
    if request.method == 'POST':
        return create_users(request)

    return empty_form(request)


def create_users(request):
    form = UserForm(request.POST)
    if not form.is_valid():
        return empty_form(request)

    User.objects.create_user(username=form.cleaned_data.get("username"),
                             email=form.cleaned_data.get("email"),
                             password=form.cleaned_data.get("password"))

    return HttpResponseRedirect(r('usuario:login'))


def validar(request, sucesso=SUCESSO):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect(r(sucesso))
    else:
        messages.success(request, 'usuario não autenticado')

    return HttpResponseRedirect(r('usuario:login'))


def empty_form(request):
    return render(request, 'usuario/form_cadastro.html', {'form': UserForm()})
