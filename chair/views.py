import re

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views import View

from chair.forms import UserRegistrationForm, LoginForm
from chair.models import ChairModel


class HomeView(View):

    def get(self, request):
        form = LoginForm()
        if request.user.is_authenticated:
            current_user = request.user.username
            query_user = re.findall(r'[^\@]+', current_user)
            speciality = query_user[0]
            hospital = query_user[1]
            chair = ChairModel.objects.all()
            return render(request=request, template_name='chair/homepage.html',
                          context={'especialidad': speciality,
                                   'nombre_del_hospital': hospital,
                                   'chair': chair,
                                   })
        return render(request=request, template_name='chair/homepage.html', context={'authentication_form': form})

    def post(self, request):
        form = LoginForm()
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('home')
        return render(request=request, template_name='chair/homepage.html',
                      context={'authentication_form': form,
                               'error': 'Los datos son incorrectos. Intenta otra vez por favor.'})


class RegistrationView(View):
    """Registration user view"""

    def get(self, request):
        form = UserRegistrationForm()
        return render(request=request, template_name='chair/registration.html', context={'registration_form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            ChairModel.objects.filter(estado='Libre').update(owner=request.user.id)
            return redirect('home')
        return render(request=request, template_name='chair/registration.html', context={'registration_form': form})


class LogoutView(View):

    def post(self, request):
        logout(request)
        return redirect('home')

class ChangeDestination(View):

    def post(self, request):
        chair = ChairModel.objects.filter(owner=request.user)[0].estado
        if chair == 'Libre':
            print('LIBRE!!!')
            if 'oncologia' in request.POST:
                ChairModel.objects.filter(owner=request.user).update(estado='Ocupado')
                ChairModel.objects.filter(owner=request.user).update(destino='Oncologia')
            if 'radiologia' in request.POST:
                ChairModel.objects.filter(owner=request.user).update(estado='Ocupado')
                ChairModel.objects.filter(owner=request.user).update(destino='Radiologia')
            if 'farmacia' in request.POST:
                ChairModel.objects.filter(owner=request.user).update(estado='Ocupado')
                ChairModel.objects.filter(owner=request.user).update(destino='Farmacia')
            return redirect('home')
        if 'en_blanco' in request.POST:
            ChairModel.objects.filter(owner=request.user).update(estado='Libre', destino='"En blanco"', ubicacion='Estacion de carga')
        return redirect('home')
