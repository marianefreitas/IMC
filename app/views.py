from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_user(request):
    if request.method == 'GET':
        return render(request, 'login.html', {})
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'dashboard.html', {})
        else:
            messages.warning(request, ('Usuário não encontrado!'))
            return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, ("Você foi desloado com sucesso"))
    return redirect('home')


def home(request):
    return render(request, 'index.html', {})


def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html', {})
    else:
        messages.warning(request, ('Faça seu login!'))
        return render(request, 'login.html', {})
