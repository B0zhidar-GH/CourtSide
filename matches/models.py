from django.conf import settings
from django.db import models

from tournaments.models import Tournament


class Match(models.Model):

    class Status(models.TextChoices):
        SCHEDULED = "scheduled", "Scheduled"
        IN_PROGRESS = "in_progress", "In progress"
        COMPLETED = "completed", "Completed"

    tournament = models.ForeignKey( Tournament, on_delete=models.CASCADE, related_name="matches")

    player1 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="matches_as_player1")

    player2 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="matches_as_player2")

    winner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="matches_won")

    round_number = models.PositiveIntegerField(default=1)
    scheduled_at = models.DateTimeField(null=True, blank=True)

    status = models.CharField(max_length=20, choices=Status.choices, default=Status.SCHEDULED)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tournament} - Round {self.round_number}"


class MatchSet(models.Model):

    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name="sets",)

    set_number = models.PositiveIntegerField()
    player1_games = models.PositiveIntegerField()
    player2_games = models.PositiveIntegerField()

    class Meta:
        ordering = ["set_number"]

        constraints = [models.UniqueConstraint(fields=["match", "set_number"], name="unique_match_set_number")]

    def __str__(self):
        return f"Set {self.set_number} - {self.match}"