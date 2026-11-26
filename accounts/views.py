import profile

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic import FormView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import RegisterForm, PlayerProfileForm
from .models import PlayerProfile

# Create your views here.

class RegisterView(FormView):

    template_name = 'accounts/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):

        user = form.save()

        PlayerProfile.objects.create(user=user)

        login(self.request, user)

        return super().form_valid(form)

class AccountLogInView(LoginView):
    template_name = 'accounts/login.html'

class AccountLogOutView(LogoutView):
    #template_name = 'accounts/logout.html'
    next_page = 'home'

class PlayerProfileView(LoginRequiredMixin, UpdateView):

    model = PlayerProfile
    form_class = PlayerProfileForm
    template_name = 'accounts/profile.html'
    success_url = reverse_lazy('profile')
    login_url = 'login'

    def get_object(self, queryset = None):

        profile, created = PlayerProfile.objects.get_or_create(user=self.request.user)

        return profile