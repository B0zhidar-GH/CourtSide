from django.conf import settings
from django.db import models


class Tournament(models.Model):

    class Surface(models.TextChoices):
        HARD = "hard", "Hard court"
        CLAY = "clay", "Clay court"
        GRASS = "grass", "Grass court"
        INDOOR_HARD = "indoor_hard", "Indoor hard court"

    class Status(models.TextChoices):
        UPCOMING = "upcoming", "Upcoming"
        ONGOING = "ongoing", "Ongoing"
        COMPLETED = "completed", "Completed"

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, blank=True)
    location = models.CharField(max_length=100)

    surface = models.CharField(max_length=20, choices=Surface.choices)

    start_date = models.DateField()
    end_date = models.DateField()

    max_players = models.PositiveIntegerField(default=16)

    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                  related_name="organized_tournaments")

    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, through="TournamentRegistration",
                                          related_name="joined_tournaments")

    status = models.CharField(max_length=20, choices=Status.choices, default=Status.UPCOMING)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class TournamentRegistration(models.Model):

    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        APPROVED = "approved", "Approved"
        REJECTED = "rejected", "Rejected"

    tournament = models.ForeignKey(
        Tournament,
        on_delete=models.CASCADE,
        related_name="registrations",
    )

    player = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                               related_name="tournament_registrations")

    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)

    registered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["tournament", "player"], name="unique_tournament_registration")]

    def __str__(self):
        return f"{self.player} - {self.tournament}"