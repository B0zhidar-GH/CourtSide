from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView

from tournaments.models import Tournament
from .forms import MatchForm
from .models import Match

# Create your views here.

class MatchCreateView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    CreateView
):
    model = Match
    form_class = MatchForm
    template_name = "matches/match_form.html"

    def dispatch(self, request, *args, **kwargs):
        self.tournament = get_object_or_404(
            Tournament,
            pk=kwargs["pk"]
        )

        return super().dispatch(request, *args, **kwargs)

    def test_func(self):
        return self.tournament.organizer == self.request.user

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["tournament"] = self.tournament
        return kwargs

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.tournament = self.tournament
        self.object.save()

        return redirect(
            "tournament-detail",
            pk=self.tournament.pk
        )



