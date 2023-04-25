from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html')),
    path('register/', auth_views.LoginView.as_view(template_name='register.html')),
]
