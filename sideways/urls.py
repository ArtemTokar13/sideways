from django.contrib import admin
from django.urls import path

from chair.views import RegistrationView, HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('registration/', RegistrationView.as_view(), name='registration'),
]
