
from django import forms
from django.contrib.auth import get_user_model

from .models import Match
from tournaments.models import TournamentRegistration


User = get_user_model()


class MatchForm(forms.ModelForm):

    class Meta:
        model = Match
        fields = [
            "player1",
            "player2",
            "round_number",
            "scheduled_at",
        ]

        labels = {
            "player1": "First player",
            "player2": "Second player",
            "round_number": "Round number",
            "scheduled_at": "Scheduled date and time",
        }

        help_texts = {
            "player1": "Choose an approved tournament participant.",
            "player2": "Choose a different approved participant.",
            "round_number": "Enter the tournament round.",
            "scheduled_at": "Choose when the match will be played.",
        }

        widgets = {
            "scheduled_at": forms.DateTimeInput(
                attrs={"type": "datetime-local"},
                format="%Y-%m-%dT%H:%M",
            ),
        }

    def __init__(self, *args, tournament, **kwargs):
        super().__init__(*args, **kwargs)

        self.tournament = tournament

        approved_players = User.objects.filter(
            tournament_registrations__tournament=tournament,
            tournament_registrations__status=(
                TournamentRegistration.Status.APPROVED
            ),
        ).distinct()

        self.fields["player1"].queryset = approved_players
        self.fields["player2"].queryset = approved_players

        self.fields["player1"].empty_label = "Select first player"
        self.fields["player2"].empty_label = "Select second player"

        self.fields["scheduled_at"].input_formats = [
            "%Y-%m-%dT%H:%M"
        ]

    def clean(self):
        cleaned_data = super().clean()

        player1 = cleaned_data.get("player1")
        player2 = cleaned_data.get("player2")

        if player1 and player2 and player1 == player2:
            self.add_error(
                "player2",
                "The two players must be different."
            )

        return cleaned_data
