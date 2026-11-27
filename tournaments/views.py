from lib2to3.fixes.fix_input import context

from django.db.models import Model
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (TemplateView, ListView, DetailView, CreateView,
                                  UpdateView, DeleteView, FormView)

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.views.decorators.http import require_POST
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

import tournaments
#from django

from .models import Tournament, TournamentRegistration
from .forms import TournamentForm, TournamentRegistrationForm

# Create your views here.

class HomeView(TemplateView):

    template_name = 'home.html'


class TournamentListView(ListView):

    model = Tournament
    template_name = 'tournaments/tournament_list.html'
    context_object_name = 'tournaments'
    ordering = ('start_date',)

class TournamentDetailView(DetailView):

    model = Tournament
    template_name = 'tournaments/tournament_detail.html'
    context_object_name = 'tournament'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            registration = (TournamentRegistration.objects.
                            filter(tournament=self.object, player=self.request.user).first())

        else:
            registration = None

        context['registration'] = registration

        return context

class TournamentCreateView(LoginRequiredMixin, CreateView):

    model = Tournament
    form_class = TournamentForm
    template_name = 'tournaments/tournament_form.html'
    success_url = reverse_lazy('tournament-list')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.organizer = self.request.user
        return super().form_valid(form)

class TournamentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = Tournament
    form_class = TournamentForm
    template_name = 'tournaments/tournament_edit.html'
    context_object_name = 'tournament'

    def test_func(self):
        tournament = self.get_object()

        return tournament.organizer == self.request.user

    def get_success_url(self):

        return reverse_lazy('tournament-detail', kwargs={'pk': self.object.pk})

class TournamentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    model = Tournament
    template_name = 'tournaments/tournament_confirm_delete.html'
    context_object_name = 'tournament'
    success_url = reverse_lazy('tournament-list')

    def test_func(self):
        tournament = self.get_object()

        return tournament.organizer == self.request.user

class TournamentRegisterView(LoginRequiredMixin, FormView):

    template_name = 'tournaments/tournament_register.html'
    form_class = TournamentRegistrationForm
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):

        self.tournament = get_object_or_404(Tournament, pk=kwargs['pk'])

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        TournamentRegistration.objects.get_or_create(tournament=self.tournament, player=self.request.user,
                                                     defaults={'status': 'pending'})

        return redirect('tournament-detail', pk=self.tournament.pk)

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['tournament'] = self.tournament

        return context

class TournamentRegistrationView(LoginRequiredMixin, UserPassesTestMixin, ListView):

    model = TournamentRegistration
    template_name = 'tournaments/tournament_registration.html'
    context_object_name = 'registrations'

    def dispatch(self, request, *args, **kwargs):

        self.tournament = get_object_or_404(
            Tournament,
            pk=kwargs['pk']
        )

        return super().dispatch(request, *args, **kwargs)

    def test_func(self):

        return self.tournament.organizer == self.request.user

    def get_queryset(self):

        return (TournamentRegistration.objects.filter(tournament=self.tournament)
                .select_related('player'))

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['tournament'] = self.tournament

        return context

@login_required
@require_POST
def manage_registration(request, pk, registration_pk):

    tournament = get_object_or_404(Tournament, pk=pk)

    if tournament.organizer != request.user:
        return HttpResponseForbidden('You are not allowed to manage this page!')

    registration = get_object_or_404(TournamentRegistration,
                                     pk=registration_pk, tournament=tournament)

    action = request.POST.get('action')

    if action == 'approve':
        registration.status = 'approved'
        registration.save()

    elif action == 'reject':
        registration.status = 'rejected'
        registration.save()

    return redirect(
        'tournament-registrations',
        pk=tournament.pk
    )