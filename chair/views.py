from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views import View

from chair.forms import UserRegistrationForm


class HomeView(View):

    def get(self, request):
        return render(request=request, template_name='chair/homepage.html')

class RegistrationView(View):
    """Registration user view"""

    def get(self, request):
        form = UserRegistrationForm()
        return render(request=request, template_name='chair/registration.html', context={'register_form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        return render(request=request, template_name='chair/registration.html', context={'registration_form': form})