from django.conf import settings
from django.db import models


class RankingSeason(models.Model):

    name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()

    players = models.ManyToManyField(settings.AUTH_USER_MODEL, through="RankingEntry", related_name="ranking_seasons")

    def __str__(self):
        return self.name


class RankingEntry(models.Model):

    season = models.ForeignKey(RankingSeason, on_delete=models.CASCADE, related_name="entries")

    player = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="ranking_entries",)

    points = models.PositiveIntegerField(default=0)
    matches_played = models.PositiveIntegerField(default=0)
    wins = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["-points"]

        constraints = [models.UniqueConstraint(fields=["season", "player"], name="unique_player_ranking_per_season")]

    def __str__(self):
        return f"{self.player} - {self.points} points"