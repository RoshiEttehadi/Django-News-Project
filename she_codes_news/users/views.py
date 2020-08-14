from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.edit import FormView
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView

from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm
from .forms import CustomUserChangeForm

from django.db import models
from django.contrib.auth import get_user_model


class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

class UserView(generic.DetailView):
    model = CustomUser
    template_name = 'users/userProfile.html'
    context_object_name = 'users'


class AuthorView(generic.DetailView):
    model = CustomUser
    template_name = 'users/authorView.html'
    context_object_name = 'author'    


