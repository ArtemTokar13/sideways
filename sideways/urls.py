from django.contrib import admin
from django.urls import path

from chair.views import RegistrationView, HomeView, LogoutView#, ChangeDestination

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('logout/', LogoutView.as_view(), name='logout'),
    #path('change_destination/', ChangeDestination.as_view(), name='change_destination')
]
